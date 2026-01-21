import React, { useState } from 'react';
import ImageUpload from '../components/ImageUpload';
import { analyzeImage } from '../api/client';

const Home: React.FC = () => {
  const [fen, setFen] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleUpload = async (file: File) => {
    setLoading(true);
    setError(null);
    setFen(null);
    try {
      // For US1, we ignore activeColor (defaults to 'w' in client)
      const result = await analyzeImage(file);
      setFen(result.fen);
    } catch (err) {
      console.error(err);
      const errorMessage = err instanceof Error ? err.message : 'An error occurred during analysis';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      <div className="text-center">
        <h2 className="text-2xl font-bold text-gray-900">Upload Chess Puzzle</h2>
        <p className="mt-2 text-gray-600">
          Upload a clear photo of a chessboard to generate its FEN notation.
        </p>
      </div>

      <ImageUpload onFileSelect={handleUpload} isLoading={loading} />

      {error && (
        <div className="bg-red-50 text-red-700 p-4 rounded-md border border-red-200 max-w-xl mx-auto">
          {error}
        </div>
      )}

      {fen && (
        <div className="bg-green-50 p-6 rounded-lg border border-green-200 max-w-xl mx-auto">
          <h3 className="text-lg font-medium text-green-900 mb-2">Result FEN:</h3>
          <p className="font-mono bg-white p-3 rounded border border-green-300 break-all select-all text-gray-800">
            {fen}
          </p>
        </div>
      )}
    </div>
  );
};

export default Home;
