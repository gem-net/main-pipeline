import { useState } from "react";

export default function Upload() {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append("files", file);

        const response = await fetch("http://localhost:8000/uploadfiles/", {
            method: "POST",
            body: formData,
        });

        const data = await response.json();
        console.log(data);
    };

    const handleDownloadTNA = () => {
        window.open("http://localhost:8000/download/tRNA/", "_blank");
    };

    const handleDownloadSynthetase = () => {
        window.open("http://localhost:8000/download/synthetase/", "_blank");
    };

    const handleDownloadCompounds = () => {
        window.open("http://localhost:8000/download/compounds/", "_blank");
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            <p></p>
            <button onClick={handleDownloadTNA}>Download tRNA</button>
            <button onClick={handleDownloadSynthetase}>
                Download Synthetase
            </button>
            <button onClick={handleDownloadCompounds}>
                Download Compounds
            </button>
        </div>
    );
}
