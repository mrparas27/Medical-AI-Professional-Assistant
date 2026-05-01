import React from 'react'
import { MessageCircle, Trash2, Download } from 'lucide-react'

export default function ChatMessage({ message, onDeleteMessage }) {
  const isUser = message.role === 'user'
  const timestamp = new Date(message.timestamp).toLocaleTimeString()

  return (
    <div className={`mb-4 flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div
        className={`max-w-xs lg:max-w-md xl:max-w-lg px-4 py-3 rounded-lg ${
          isUser
            ? 'bg-blue-500 text-white rounded-br-none'
            : 'bg-gray-100 text-gray-800 rounded-bl-none border border-gray-200'
        }`}
      >
        <p className="text-sm break-words">{message.content}</p>
        <div className="flex items-center justify-between mt-2 gap-2">
          <span className={`text-xs opacity-70 ${isUser ? 'text-blue-100' : 'text-gray-600'}`}>
            {timestamp}
          </span>
          {message.confidence && !isUser && (
            <span className="text-xs opacity-70 bg-opacity-20 bg-gray-500 px-2 py-1 rounded">
              Confidence: {(message.confidence * 100).toFixed(0)}%
            </span>
          )}
          {onDeleteMessage && (
            <button
              onClick={() => onDeleteMessage(message.id)}
              className={`p-1 hover:opacity-70 transition ${
                isUser ? 'hover:bg-blue-400' : 'hover:bg-gray-200'
              } rounded`}
              title="Delete message"
            >
              <Trash2 size={14} />
            </button>
          )}
        </div>
      </div>
    </div>
  )
}
