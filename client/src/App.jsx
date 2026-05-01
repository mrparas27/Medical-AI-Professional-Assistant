import React, { useState, useRef, useEffect } from 'react'
import { Send, Settings, Download, Menu, X } from 'lucide-react'
import { askQuestion } from './services/api'
import { useVoiceRecorder } from './hooks/useVoiceRecorder'
import ChatMessage from './components/ChatMessage'
import VoiceInput from './components/VoiceInput'
import PDFUpload from './components/PDFUpload'
import './index.css'

export default function App() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [sidebarOpen, setSidebarOpen] = useState(true)
  const [activeTab, setActiveTab] = useState('chat')
  const messagesEndRef = useRef(null)
  const { isRecording, transcript, isProcessing, startRecording, stopRecording, clearTranscript } = useVoiceRecorder()

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  const handleSendMessage = async (e) => {
    e.preventDefault()
    if (!input.trim() || isLoading) return

    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: input,
      timestamp: new Date().toISOString(),
    }

    setMessages((prev) => [...prev, userMessage])
    setInput('')
    setIsLoading(true)

    try {
      const response = await askQuestion(input)
      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: response.response || 'No response generated',
        confidence: response.confidence || 0,
        timestamp: new Date().toISOString(),
      }
      setMessages((prev) => [...prev, assistantMessage])
    } catch (error) {
      const errorMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: `❌ Error: ${error.message}. Make sure the server is running on http://127.0.0.1:8000`,
        timestamp: new Date().toISOString(),
      }
      setMessages((prev) => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
    }
  }

  const handleVoiceTranscript = (text) => {
    setInput(text)
  }

  const handleClearChat = () => {
    if (window.confirm('Clear all chat history?')) {
      setMessages([])
    }
  }

  const handleExportChat = () => {
    const dataStr = JSON.stringify(messages, null, 2)
    const dataBlob = new Blob([dataStr], { type: 'application/json' })
    const url = URL.createObjectURL(dataBlob)
    const link = document.createElement('a')
    link.href = url
    link.download = `chat_${new Date().toISOString().split('T')[0]}.json`
    link.click()
  }

  const handleDeleteMessage = (id) => {
    setMessages((prev) => prev.filter((msg) => msg.id !== id))
  }

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div
        className={`${
          sidebarOpen ? 'w-80' : 'w-0'
        } bg-gradient-to-b from-blue-900 to-blue-800 text-white transition-all duration-300 overflow-hidden flex flex-col`}
      >
        <div className="p-6 border-b border-blue-700">
          <h1 className="text-2xl font-bold flex items-center gap-2">
            <span className="text-3xl">🩺</span>
            Medical AI
          </h1>
          <p className="text-sm text-blue-200 mt-1">Professional Assistant</p>
        </div>

        <div className="flex-1 overflow-y-auto p-4">
          {/* Tabs */}
          <div className="space-y-2 mb-6">
            <button
              onClick={() => setActiveTab('chat')}
              className={`w-full text-left px-4 py-2 rounded-lg font-semibold transition ${
                activeTab === 'chat'
                  ? 'bg-blue-700 text-white'
                  : 'text-blue-100 hover:bg-blue-700'
              }`}
            >
              💬 Chat
            </button>
            <button
              onClick={() => setActiveTab('upload')}
              className={`w-full text-left px-4 py-2 rounded-lg font-semibold transition ${
                activeTab === 'upload'
                  ? 'bg-blue-700 text-white'
                  : 'text-blue-100 hover:bg-blue-700'
              }`}
            >
              📄 Documents
            </button>
            <button
              onClick={() => setActiveTab('voice')}
              className={`w-full text-left px-4 py-2 rounded-lg font-semibold transition ${
                activeTab === 'voice'
                  ? 'bg-blue-700 text-white'
                  : 'text-blue-100 hover:bg-blue-700'
              }`}
            >
              🎤 Voice
            </button>
          </div>

          {/* Tab Content */}
          {activeTab === 'chat' && (
            <div className="space-y-3">
              <button
                onClick={handleClearChat}
                className="w-full bg-red-600 hover:bg-red-700 text-white py-2 px-4 rounded-lg font-semibold transition"
              >
                🗑️ Clear Chat
              </button>
              <button
                onClick={handleExportChat}
                disabled={messages.length === 0}
                className="w-full bg-green-600 hover:bg-green-700 disabled:opacity-50 text-white py-2 px-4 rounded-lg font-semibold transition"
              >
                💾 Export Chat
              </button>
              <div className="bg-blue-700 rounded-lg p-3">
                <p className="text-sm font-semibold mb-2">Session Stats</p>
                <div className="space-y-1 text-sm">
                  <p>
                    Questions: {messages.filter((m) => m.role === 'user').length}
                  </p>
                  <p>
                    Responses: {messages.filter((m) => m.role === 'assistant').length}
                  </p>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'upload' && (
            <div>
              <PDFUpload onUploadSuccess={() => setActiveTab('chat')} />
            </div>
          )}

          {activeTab === 'voice' && (
            <div>
              <VoiceInput
                onTranscript={handleVoiceTranscript}
                isRecording={isRecording}
                transcript={transcript}
                isProcessing={isProcessing}
                onClear={clearTranscript}
                onStop={stopRecording}
                onStart={startRecording}
              />
            </div>
          )}
        </div>

        <div className="p-4 border-t border-blue-700 text-xs text-blue-200">
          <p>Server: http://127.0.0.1:8000</p>
          <p>Status: {isLoading ? '🔄 Processing' : '✅ Ready'}</p>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 flex flex-col">
        {/* Header */}
        <div className="bg-white border-b border-gray-200 px-6 py-4 flex items-center justify-between">
          <button
            onClick={() => setSidebarOpen(!sidebarOpen)}
            className="p-2 hover:bg-gray-100 rounded-lg transition"
          >
            {sidebarOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
          <h2 className="text-2xl font-bold text-gray-800">🩺 Medical Assistant</h2>
          <div className="w-10" />
        </div>

        {/* Chat Area */}
        <div className="flex-1 overflow-y-auto p-6 space-y-4">
          {messages.length === 0 ? (
            <div className="h-full flex items-center justify-center">
              <div className="text-center">
                <div className="text-6xl mb-4">🩺</div>
                <h3 className="text-2xl font-bold text-gray-700 mb-2">
                  Welcome to Medical Assistant
                </h3>
                <p className="text-gray-500 mb-6 max-w-md">
                  Upload your medical documents, ask questions, and get intelligent responses powered by AI
                </p>
                <div className="space-y-2 text-sm text-gray-600">
                  <p>✨ Fast & Secure</p>
                  <p>🎤 Voice Support</p>
                  <p>📄 Document Analysis</p>
                </div>
              </div>
            </div>
          ) : (
            <>
              {messages.map((message) => (
                <ChatMessage
                  key={message.id}
                  message={message}
                  onDeleteMessage={handleDeleteMessage}
                />
              ))}
              {isLoading && (
                <div className="flex justify-start">
                  <div className="bg-gray-100 rounded-lg p-4 border border-gray-200">
                    <div className="flex gap-2">
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                    </div>
                  </div>
                </div>
              )}
              <div ref={messagesEndRef} />
            </>
          )}
        </div>

        {/* Input Area */}
        <div className="bg-white border-t border-gray-200 p-6">
          <form onSubmit={handleSendMessage} className="space-y-3">
            <div className="flex gap-3">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask your medical question..."
                disabled={isLoading}
                className="flex-1 px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:bg-gray-50"
              />
              <button
                type="submit"
                disabled={isLoading || !input.trim()}
                className="bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 disabled:opacity-50 text-white px-6 py-3 rounded-lg font-semibold flex items-center gap-2 transition"
              >
                <Send size={20} />
                Send
              </button>
            </div>
            {transcript && (
              <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                <div className="text-sm text-blue-600 mb-2">Voice input ready:</div>
                <p className="text-gray-700">{transcript}</p>
                <button
                  type="button"
                  onClick={() => {
                    setInput(transcript)
                    clearTranscript()
                  }}
                  className="mt-2 text-sm bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded transition"
                >
                  Use This
                </button>
              </div>
            )}
          </form>
        </div>
      </div>
    </div>
  )
}
