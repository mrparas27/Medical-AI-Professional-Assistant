import { useState, useCallback, useRef } from 'react'

export const useVoiceRecorder = () => {
  const [isRecording, setIsRecording] = useState(false)
  const [transcript, setTranscript] = useState('')
  const [isProcessing, setIsProcessing] = useState(false)
  const recognitionRef = useRef(null)
  const finalTranscriptRef = useRef('')

  const startRecording = useCallback(() => {
    // Web Speech API
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    if (!SpeechRecognition) {
      alert('Speech Recognition not supported in your browser')
      return
    }

    // Reset transcript
    finalTranscriptRef.current = ''
    setTranscript('')

    const recognition = new SpeechRecognition()
    recognition.continuous = false
    recognition.interimResults = true
    recognition.lang = 'en-US'

    recognition.onstart = () => {
      setIsRecording(true)
      setIsProcessing(true)
    }

    recognition.onresult = (event) => {
      let interimTranscript = ''
      
      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript
        if (event.results[i].isFinal) {
          // Only add if not already in final transcript (prevents duplication)
          if (!finalTranscriptRef.current.includes(transcript)) {
            finalTranscriptRef.current += transcript + ' '
          }
        } else {
          interimTranscript += transcript
        }
      }
      
      // Update display with final + interim
      setTranscript(finalTranscriptRef.current + interimTranscript)
    }

    recognition.onerror = (event) => {
      console.error('Speech recognition error:', event.error)
      setIsProcessing(false)
    }

    recognition.onend = () => {
      setIsRecording(false)
      setIsProcessing(false)
      // Set final transcript
      setTranscript(finalTranscriptRef.current.trim())
    }

    recognitionRef.current = recognition
    recognition.start()
  }, [])

  const stopRecording = useCallback(() => {
    if (recognitionRef.current) {
      recognitionRef.current.stop()
    }
  }, [])

  const clearTranscript = useCallback(() => {
    setTranscript('')
  }, [])

  return {
    isRecording,
    isProcessing,
    transcript,
    startRecording,
    stopRecording,
    clearTranscript,
  }
}
