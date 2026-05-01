import React from 'react'
import { Mic, Square, Copy, Trash2 } from 'lucide-react'

export default function VoiceInput({ onTranscript, isRecording, transcript, isProcessing, onClear, onStop, onStart }) {
  const handleCopyTranscript = () => {
    navigator.clipboard.writeText(transcript)
  }

  const handleUseTranscript = () => {
    if (transcript.trim()) {
      onTranscript(transcript.trim())
      onClear()
    }
  }

  return (
    <div className="space-y-3">
      <div className="flex gap-2">
        {!isRecording ? (
          <button
            onClick={onStart}
            disabled={isProcessing}
            className="flex-1 flex items-center justify-center gap-2 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white py-2 px-4 rounded-lg font-semibold transition disabled:opacity-50"
          >
            <Mic size={20} />
            Start Recording
          </button>
        ) : (
          <button
            onClick={onStop}
            className="flex-1 flex items-center justify-center gap-2 bg-gradient-to-r from-red-500 to-red-600 hover:from-red-600 hover:to-red-700 text-white py-2 px-4 rounded-lg font-semibold transition animate-pulse"
          >
            <Square size={20} />
            Stop Recording
          </button>
        )}
      </div>

      {transcript && (
        <div className="bg-gray-50 rounded-lg p-3 border border-gray-200">
          <div className="text-sm text-gray-600 mb-2">Transcript:</div>
          <p className="text-gray-700 mb-3">{transcript}</p>
          <div className="flex gap-2">
            <button
              onClick={handleUseTranscript}
              className="flex-1 bg-green-500 hover:bg-green-600 text-white py-1 px-3 rounded text-sm font-semibold transition"
            >
              Use This
            </button>
            <button
              onClick={handleCopyTranscript}
              className="px-3 py-1 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded text-sm transition"
              title="Copy to clipboard"
            >
              <Copy size={16} />
            </button>
            <button
              onClick={onClear}
              className="px-3 py-1 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded text-sm transition"
              title="Clear transcript"
            >
              <Trash2 size={16} />
            </button>
          </div>
        </div>
      )}

      {isProcessing && (
        <div className="text-center text-sm text-blue-600 animate-pulse">
          🎤 Listening...
        </div>
      )}
    </div>
  )
}
