from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
import csv
from typing import Annotated
import PyPDF2
from io import BytesIO
from typing import List
import pandas as pd
import os
from collections import defaultdict

from utils.get_doi import get_metadata_from_doi, generate_jacs_citation
from utils.extract_tRNA import extract_tRNA
from utils.extract_compounds import extract_compounds
from utils.extract_synthetase import extract_synthetase

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
UPLOAD_FOLDER = "uploaded_files"
OUPUT_FOLDER = 'output'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://vercel.com/jayyeung/CGEM-main-pipeline-frontend"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/hello")
def hello_world():
    return {"message": "Hello World"}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    file_contents = defaultdict(list)

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    for file in files:
        content = await file.read()
        filename = file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        
        print(content)
        
        with open(file_path, "wb") as buffer:
            buffer.write(content)
        
        if filename.endswith('.pdf'):
            try:
                pdf_reader = PyPDF2.PdfFileReader(file_path)
                for page_num in range(pdf_reader.numPages):
                    page = pdf_reader.getPage(page_num)
                    text = page.extract_text()
                    file_contents[filename].append(text)
            except Exception as e:
                file_contents[filename] = f"Could not read PDF: {e}"
        else:
            file_contents[filename] = "Unsupported file type"
    
    update_downloads(list(file_contents.values())[0])

    return JSONResponse(content={"file_contents": file_contents})

def update_downloads(full_text: List[str]): 
    tRNA = []
    synthetase = []
    compounds = []

    for page_num, text in enumerate(full_text):
        tRNA.extend(extract_tRNA(text, page = page_num))
        synthetase.extend(extract_synthetase(text, page = page_num))
        compounds.extend(extract_compounds(text, page = page_num))

    print(tRNA)
    print(synthetase)
    print(compounds)
    
    if not os.path.exists(OUPUT_FOLDER):
        os.makedirs(OUPUT_FOLDER)

    tRNA_df = pd.DataFrame(tRNA)
    tRNA_df.to_csv(f'{OUPUT_FOLDER}/tRNA.csv')

    synthetase_df = pd.DataFrame(synthetase)
    synthetase_df.to_csv(f'{OUPUT_FOLDER}/synthetase.csv')

    compounds_df = pd.DataFrame(compounds)
    compounds_df.to_csv(f'{OUPUT_FOLDER}/compounds.csv')

@app.get("/download/tRNA/")
async def download_tRNA():
    filename = f"{OUPUT_FOLDER}/tRNA.csv"
    return FileResponse(
        filename,
        headers={
            "Content-Disposition": f"attachment; filename=tRNA.csv", 
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )

@app.get("/download/synthetase/")
async def download_synthetase():
    filename = f"{OUPUT_FOLDER}/synthetase.csv"
    return FileResponse(
        filename,
        headers={
            "Content-Disposition": f"attachment; filename=synthetase.csv", 
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )

@app.get("/download/compounds/")
async def download_compounds():
    filename = f"{OUPUT_FOLDER}/compounds.csv"
    return FileResponse(
        filename,
        headers={
            "Content-Disposition": f"attachment; filename=compounds.csv", 
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0"
        }
    )