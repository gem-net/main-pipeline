## Features

-   **File Upload**: Users can upload research papers in PDF format.
-   **Data Extraction**: Extracts specific information like tRNA, synthetase, and compounds from the uploaded PDFs.
-   **File Download**: Users can download the extracted data in CSV format.

## Installation

### Backend

1. Navigate to the project directory.

2. Run the FastAPI server:
    ```bash
    npm run fastapi-dev
    ```

### Frontend

1. Navigate to the project directory.
2. Install the required npm packages:

    ```bash
    npm install
    ```

3. Run the Next.js development server:

    ```bash
    npm run next-dev
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:3000` for the frontend.
2. Navigate to `http://localhost:8000/docs` for the FastAPI generated documentation.

## API Endpoints

-   `GET /api/hello`: Returns a Hello World message.
-   `POST /uploadfiles/`: Accepts file uploads and processes them.
-   `GET /download/tRNA/`: Downloads the tRNA data as a CSV.
-   `GET /download/synthetase/`: Downloads the synthetase data as a CSV.
-   `GET /download/compounds/`: Downloads the compounds data as a CSV.
