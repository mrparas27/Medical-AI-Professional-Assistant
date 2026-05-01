# React Medical Assistant

A modern, professional React-based UI for the Medical Assistant application.

## Features

- 🎨 Modern, responsive design with Tailwind CSS
- 🎤 Fast voice-to-text using Web Speech API (no server wait)
- 📄 Drag-and-drop PDF upload
- 💬 Real-time chat with confidence scores
- 📊 Session statistics
- 💾 Export chat history
- 🎯 Tab-based interface

## Quick Start

### 1. Install Dependencies

```bash
cd client
npm install
```

### 2. Start Development Server

```bash
npm run dev
```

The app will be available at `http://localhost:3000`

### 3. Build for Production

```bash
npm run build
```

## Project Structure

```
src/
├── components/         # React components
│   ├── ChatMessage.jsx
│   ├── VoiceInput.jsx
│   └── PDFUpload.jsx
├── hooks/              # Custom React hooks
│   └── useVoiceRecorder.js
├── services/           # API services
│   └── api.js
├── App.jsx             # Main component
└── index.css           # Global styles
```

## Configuration

- Backend API: `http://127.0.0.1:8000`
- Frontend Port: `3000`
- Proxy: API calls are proxied to backend

## Browser Requirements

- Modern browser with Web Speech API support
- Chrome, Edge, Firefox (latest versions recommended)

## Performance Notes

- Voice recording uses browser's native Web Speech API (instant results)
- No server-side voice processing delay
- Optimized re-renders with React hooks
- Lazy loading for heavy components
