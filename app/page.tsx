import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100 dark:bg-gray-900">
      <div className="container mx-auto p-8">
        <h1 className="text-4xl font-bold text-center my-8">
          Welcome to the CGEM Research Paper Processing App
        </h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Link to Upload Page */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
            <h2 className="text-2xl font-bold mb-4">File Upload</h2>
            <p className="mb-4">Users can upload research papers in PDF format and extract specific information like tRNA, synthetase, and compounds.</p>
            <Link href="/upload" legacyBehavior>
              <a className="inline-block bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors">
                Go to Upload
              </a>
            </Link>
          </div>

          {/* Link to DOI Page */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
            <h2 className="text-2xl font-bold mb-4">DOI Citation Fetching</h2>
            <p className="mb-4">Users can enter a DOI to fetch and generate the citation for the research paper.</p>
            <Link href="/doi" legacyBehavior>
              <a className="inline-block bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors">
                Go to DOI Citation
              </a>
            </Link>
          </div>

          {/* Link to Smiles Conversion Page */}
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
            <h2 className="text-2xl font-bold mb-4">IUPAC to SMILES Conversion</h2>
            <p className="mb-4">Users can convert IUPAC names to SMILES notation by uploading a CSV file.</p>
            <Link href="/smiles" legacyBehavior>
              <a className="inline-block bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors">
                Convert IUPAC to SMILES
              </a>
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
