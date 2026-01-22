import React, { useState } from 'react';
import ImageUpload from '../components/ImageUpload';
import TurnSelector from '../components/TurnSelector';
import FenDisplay from '../components/FenDisplay';
import { analyzeImage } from '../api/client';

const Home: React.FC = () => {
  const [fen, setFen] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [activeColor, setActiveColor] = useState<'w' | 'b'>('w');

  const handleUpload = async (file: File) => {
    setLoading(true);
    setError(null);
    setFen(null);
    try {
      const result = await analyzeImage(file, activeColor);
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

      <div className="max-w-xl mx-auto space-y-6">
        <TurnSelector 
          activeColor={activeColor} 
          onChange={setActiveColor} 
          disabled={loading}
        />
        
        <ImageUpload onFileSelect={handleUpload} isLoading={loading} />
      </div>

      {error && (
        <div className="bg-red-50 text-red-700 p-4 rounded-md border border-red-200 max-w-xl mx-auto">
          <div className="flex">
            <svg className="h-5 w-5 text-red-400 mr-2" viewBox="0 0 20 20" fill="currentColor">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
            </svg>
            <span className="font-medium">Analysis Failed:</span>
          </div>
          <p className="mt-1 ml-7 text-sm">{error}</p>
          <ul className="mt-2 ml-7 list-disc list-inside text-xs">
            <li>Ensure the entire chessboard is visible.</li>
            <li>Make sure the photo is taken from a top-down or slight angle.</li>
            <li>Check for good lighting and minimal glare.</li>
          </ul>
        </div>
      )}

      {fen && <FenDisplay fen={fen} />}
    </div>
  );
};

export default Home;
