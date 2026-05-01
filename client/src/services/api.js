import axios from 'axios'

const API_BASE_URL = 'http://127.0.0.1:8000/api'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000,
})

export const uploadPDFs = async (files) => {
  const formData = new FormData()
  files.forEach((file) => {
    formData.append('files', file)
  })

  try {
    const response = await api.post('/upload_pdfs/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    return response.data
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Failed to upload PDFs')
  }
}

export const askQuestion = async (question) => {
  try {
    const formData = new FormData()
    formData.append('question', question)

    const response = await api.post('/ask/', formData)
    return response.data
  } catch (error) {
    throw new Error(error.response?.data?.error || 'Failed to get response')
  }
}

export default api
