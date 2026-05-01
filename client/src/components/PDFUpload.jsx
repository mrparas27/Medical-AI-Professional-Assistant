import React, { useState } from 'react'
import { Upload, AlertCircle, CheckCircle, Loader } from 'lucide-react'
import { uploadPDFs } from '../services/api'

export default function PDFUpload({ onUploadSuccess }) {
  const [isDragging, setIsDragging] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [message, setMessage] = useState(null)

  const handleFiles = async (files) => {
    if (files.length === 0) return

    const pdfFiles = Array.from(files).filter((file) => file.type === 'application/pdf')
    if (pdfFiles.length === 0) {
      setMessage({ type: 'error', text: 'Please upload PDF files only' })
      return
    }

    setIsLoading(true)
    try {
      await uploadPDFs(pdfFiles)
      setMessage({
        type: 'success',
        text: `✅ PDF${pdfFiles.length > 1 ? 's' : ''} uploaded and indexed successfully!`,
      })
      onUploadSuccess?.()
      setTimeout(() => setMessage(null), 4000)
    } catch (error) {
      setMessage({ type: 'error', text: `❌ ${error.message}` })
    } finally {
      setIsLoading(false)
    }
  }

  const handleDragOver = (e) => {
    e.preventDefault()
    setIsDragging(true)
  }

  const handleDragLeave = (e) => {
    e.preventDefault()
    setIsDragging(false)
  }

  const handleDrop = (e) => {
    e.preventDefault()
    setIsDragging(false)
    handleFiles(e.dataTransfer.files)
  }

  const handleFileSelect = (e) => {
    handleFiles(e.target.files)
  }

  return (
    <div className="space-y-3">
      <label
        className={`block border-2 border-dashed rounded-lg p-4 text-center cursor-pointer transition ${
          isDragging
            ? 'border-blue-500 bg-blue-50'
            : 'border-gray-300 hover:border-blue-400 bg-gray-50'
        }`}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          type="file"
          multiple
          accept=".pdf"
          onChange={handleFileSelect}
          disabled={isLoading}
          className="hidden"
        />
        <div className="flex flex-col items-center gap-2">
          {isLoading ? (
            <>
              <Loader size={24} className="animate-spin text-blue-500" />
              <p className="text-sm text-gray-600">Uploading PDFs...</p>
            </>
          ) : (
            <>
              <Upload size={24} className="text-gray-600" />
              <p className="text-sm font-semibold text-gray-700">
                Drag PDFs here or click to select
              </p>
              <p className="text-xs text-gray-500">Only PDF files are supported</p>
            </>
          )}
        </div>
      </label>

      {message && (
        <div
          className={`flex items-center gap-2 p-3 rounded-lg text-sm ${
            message.type === 'error'
              ? 'bg-red-50 text-red-700 border border-red-200'
              : 'bg-green-50 text-green-700 border border-green-200'
          }`}
        >
          {message.type === 'error' ? (
            <AlertCircle size={18} />
          ) : (
            <CheckCircle size={18} />
          )}
          {message.text}
        </div>
      )}
    </div>
  )
}
