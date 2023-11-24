// doi.js
import { useState } from "react";
import "../app/globals.css";

export default function Doi() {
    const [doi, setDoi] = useState("");
    const [citation, setCitation] = useState("");

    const handleDoiChange = (e) => {
        setDoi(e.target.value);
    };

    const handleFetchCitation = async () => {
        try {
            const response = await fetch(
                `http://localhost:8000/doi?doi=${encodeURIComponent(doi)}`,
                {
                    method: "GET",
                }
            );

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            setCitation(data);
        } catch (error) {
            console.error("Error fetching citation:", error);
            setCitation("Failed to fetch citation.");
        }
    };

    return (
        <div className="container mx-auto p-4">
            <input
                type="text"
                value={doi}
                onChange={handleDoiChange}
                placeholder="Enter DOI"
                className="block w-full px-4 py-2 mt-2 mb-4 border rounded-md bg-white border-gray-300 placeholder-gray-400 text-gray-900 focus:ring-blue-500 focus:border-blue-500"
            />
            <button
                onClick={handleFetchCitation}
                className="px-4 py-2 bg-blue-500 text-white font-bold rounded hover:bg-blue-700"
            >
                Fetch Citation
            </button>
            <div
                className="mt-4 bg-gray-100 border-l-4 border-blue-500 text-gray-700 p-4"
                role="alert"
            >
                <p className="font-bold">Citation:</p>
                <p>{citation}</p>
            </div>
        </div>
    );
}
