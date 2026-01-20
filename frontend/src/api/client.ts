const API_BASE_URL = 'http://localhost:8000';

export interface AnalysisResponse {
  fen: string;
  confidence?: number;
}

export const analyzeImage = async (file: File, activeColor: string = 'w'): Promise<AnalysisResponse> => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('active_color', activeColor);

  const response = await fetch(`${API_BASE_URL}/api/analyze`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const errorData = await response.json().catch(() => ({}));
    throw new Error(errorData.detail || 'Failed to analyze image');
  }

  return response.json();
};
