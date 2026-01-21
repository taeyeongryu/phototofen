import React, { useState, ChangeEvent, DragEvent } from 'react';

interface ImageUploadProps {
  onFileSelect: (file: File) => void;
  isLoading?: boolean;
}

const ImageUpload: React.FC<ImageUploadProps> = ({ onFileSelect, isLoading = false }) => {
  const [dragActive, setDragActive] = useState(false);
  const [preview, setPreview] = useState<string | null>(null);

  const handleDrag = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e: DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    if (e.target.files && e.target.files[0]) {
      handleFile(e.target.files[0]);
    }
  };

  const handleFile = (file: File) => {
    if (!file.type.startsWith('image/')) {
      alert('Please upload an image file.');
      return;
    }
    const reader = new FileReader();
    reader.onloadend = () => {
      setPreview(reader.result as string);
    };
    reader.readAsDataURL(file);
    onFileSelect(file);
  };

  return (
    <div className="w-full max-w-xl mx-auto">
      <div
        className={`relative border-2 border-dashed rounded-lg p-8 text-center transition-colors duration-200 ease-in-out ${
          dragActive
            ? 'border-blue-500 bg-blue-50'
            : 'border-gray-300 hover:border-gray-400 bg-white'
        }`}
        onDragEnter={handleDrag}
        onDragLeave={handleDrag}
        onDragOver={handleDrag}
        onDrop={handleDrop}
      >
        <input
          type="file"
          id="image-upload"
          className="hidden"
          accept="image/*"
          onChange={handleChange}
          disabled={isLoading}
        />
        
        {preview ? (
            <div className="relative">
                <img 
                    src={preview} 
                    alt="Preview" 
                    className="mx-auto max-h-64 rounded shadow-sm"
                />
                <button 
                    onClick={(e) => {
                        e.stopPropagation();
                        e.preventDefault();
                        setPreview(null);
                        // Reset input value if needed, though uncontrolled here is fine for now
                    }}
                    className="absolute top-2 right-2 bg-red-500 text-white rounded-full p-1 hover:bg-red-600 focus:outline-none"
                    title="Remove image"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
        ) : (
            <label
            htmlFor="image-upload"
            className="cursor-pointer flex flex-col items-center justify-center h-full"
            >
            <svg
                className="mx-auto h-12 w-12 text-gray-400"
                stroke="currentColor"
                fill="none"
                viewBox="0 0 48 48"
                aria-hidden="true"
            >
                <path
                d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
                strokeWidth={2}
                strokeLinecap="round"
                strokeLinejoin="round"
                />
            </svg>
            <p className="mt-2 text-sm text-gray-600">
                <span className="font-medium text-blue-600 hover:text-blue-500">
                Upload a file
                </span>{' '}
                or drag and drop
            </p>
            <p className="mt-1 text-xs text-gray-500">PNG, JPG, GIF up to 10MB</p>
            </label>
        )}
      </div>
      {isLoading && (
          <div className="mt-4 text-center text-blue-600">
              Processing...
          </div>
      )}
    </div>
  );
};

export default ImageUpload;
