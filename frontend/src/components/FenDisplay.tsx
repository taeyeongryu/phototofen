import React, { useState } from 'react';

interface FenDisplayProps {
  fen: string;
}

const FenDisplay: React.FC<FenDisplayProps> = ({ fen }) => {
  const [copied, setCopied] = useState(false);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(fen);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy text: ', err);
    }
  };

  return (
    <div className="bg-green-50 p-6 rounded-lg border border-green-200 max-w-xl mx-auto w-full">
      <div className="flex justify-between items-center mb-2">
        <h3 className="text-lg font-medium text-green-900">Result FEN:</h3>
        <button
          onClick={handleCopy}
          className={`flex items-center space-x-1 px-3 py-1 rounded text-sm font-medium transition-colors ${
            copied
              ? 'bg-green-600 text-white'
              : 'bg-white text-gray-700 border border-gray-300 hover:bg-gray-50'
          }`}
        >
          {copied ? (
            <>
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
              <span>Copied!</span>
            </>
          ) : (
            <>
              <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3" />
              </svg>
              <span>Copy FEN</span>
            </>
          )}
        </button>
      </div>
      <div className="relative group">
        <p className="font-mono bg-white p-4 rounded border border-green-300 break-all select-all text-gray-800 text-sm shadow-inner">
          {fen}
        </p>
      </div>
    </div>
  );
};

export default FenDisplay;
