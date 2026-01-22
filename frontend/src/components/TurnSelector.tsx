import React from 'react';

interface TurnSelectorProps {
  activeColor: 'w' | 'b';
  onChange: (color: 'w' | 'b') => void;
  disabled?: boolean;
}

const TurnSelector: React.FC<TurnSelectorProps> = ({ activeColor, onChange, disabled }) => {
  return (
    <div className="flex justify-center items-center space-x-4 my-4">
      <span className="text-gray-700 font-medium">Side to Move:</span>
      <div className="flex bg-gray-100 p-1 rounded-lg">
        <button
          type="button"
          onClick={() => onChange('w')}
          disabled={disabled}
          className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
            activeColor === 'w'
              ? 'bg-white text-gray-900 shadow-sm'
              : 'text-gray-500 hover:text-gray-700'
          }`}
        >
          White
        </button>
        <button
          type="button"
          onClick={() => onChange('b')}
          disabled={disabled}
          className={`px-4 py-2 rounded-md text-sm font-medium transition-colors ${
            activeColor === 'b'
              ? 'bg-gray-800 text-white shadow-sm'
              : 'text-gray-500 hover:text-gray-700'
          }`}
        >
          Black
        </button>
      </div>
    </div>
  );
};

export default TurnSelector;
