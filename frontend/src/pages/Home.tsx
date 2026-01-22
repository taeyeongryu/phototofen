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
          {error}
        </div>
      )}

      {fen && <FenDisplay fen={fen} />}
    </div>
  );
};

export default Home;
