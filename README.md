## Features

-   **File Upload**: Users can upload research papers in PDF format.
-   **Data Extraction**: Extracts specific information like tRNA, synthetase, and compounds from the uploaded PDFs.
-   **File Download**: Users can download the extracted data in CSV format.

## Installation

### Running the app locally

1. Navigate to the project directory.

2. Make sure you have [Node.js](https://nodejs.org/en/) installed and Python 3.9 or higher.

3. Install the required npm packages:

    ```bash
    npm install
    ```

4. Run the Frontend and Backend servers:
    ```bash
    npm run dev
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:3000/upload` to upload the paper.

2. Open your web browser and navigate to `http://localhost:3000/doi` to get the citation.

### Run just Backend

1. Navigate to the project directory.

2. Run the FastAPI server:
    ```bash
    npm run fastapi-dev
    ```

### Run just Frontend

1. Navigate to the project directory.
2. Install the required npm packages:

    ```bash
    npm install
    ```

3. Run the Next.js development server:

    ```bash
    npm run next-dev
    ```

## API Endpoints

-   `GET /api/hello`: Returns a Hello World message.
-   `POST /uploadfiles/`: Accepts file uploads and processes them.
-   `GET /download/tRNA/`: Downloads the tRNA data as a CSV.
-   `GET /download/synthetase/`: Downloads the synthetase data as a CSV.
-   `GET /download/compounds/`: Downloads the compounds data as a CSV.
