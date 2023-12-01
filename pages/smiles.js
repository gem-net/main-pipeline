// smiles.js
import { useState } from "react";
import "../app/globals.css";

export default function Smiles() {
    const [file, setFile] = useState(null);
    const [downloadLink, setDownloadLink] = useState("");

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleConvertSmiles = async () => {
        try {
            const formData = new FormData();
            formData.append("file", file);

            const response = await fetch(`http://localhost:8000/smiles`, {
                method: "POST",
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            // Since we're expecting a file, we need to handle the response differently
            const blob = await response.blob();
            const downloadUrl = window.URL.createObjectURL(blob);
            setDownloadLink(downloadUrl);
        } catch (error) {
            console.error("Error converting to SMILES:", error);
        }
    };

    return (
        <div className="container mx-auto p-4">
            <input
                type="file"
                onChange={handleFileChange}
                className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100"
            />
            <button
                onClick={handleConvertSmiles}
                className="mt-4 px-4 py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-700"
            >
                Convert to SMILES
            </button>
            {downloadLink && (
                <a
                    href={downloadLink}
                    download="smiles_converted.csv"
                    className="mt-4 block px-4 py-2 bg-green-500 text-white font-bold rounded hover:bg-green-700"
                >
                    Download Converted File
                </a>
            )}
        </div>
    );
}
