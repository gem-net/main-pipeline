import { useState } from "react";
import "../app/globals.css";

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
        <div className="container mx-auto p-4">
            <input
                type="file"
                onChange={handleFileChange}
                className="block w-full text-sm text-gray-500
            file:mr-4 file:py-2 file:px-4
            file:rounded-full file:border-0
            file:text-sm file:font-semibold
            file:bg-violet-50 file:text-violet-700
            hover:file:bg-violet-100"
            />
            <button
                onClick={handleUpload}
                className="mt-4 px-4 py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-700"
            >
                Upload
            </button>
            <div className="mt-4">
                <button
                    onClick={handleDownloadTNA}
                    className="px-4 py-2 bg-green-500 text-white font-bold rounded hover:bg-green-700 mr-2"
                >
                    Download tRNA
                </button>
                <button
                    onClick={handleDownloadSynthetase}
                    className="px-4 py-2 bg-green-500 text-white font-bold rounded hover:bg-green-700 mr-2"
                >
                    Download Synthetase
                </button>
                <button
                    onClick={handleDownloadCompounds}
                    className="px-4 py-2 bg-green-500 text-white font-bold rounded hover:bg-green-700"
                >
                    Download Compounds
                </button>
            </div>
        </div>
    );
}
