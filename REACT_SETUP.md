# 🩺 Medical Assistant - React UI Guide

## Quick Setup & Run Commands

### ✅ Prerequisites

- **Node.js** 16+ (Download from https://nodejs.org/)
- **Python** 3.8+ (for backend)
- **Backend API** running on `http://127.0.0.1:8000`

---

## 🚀 Quick Start (Recommended)

### For Windows:

```bash
# Run everything with one command
run_full_stack.bat
```

### For macOS/Linux:

```bash
# Run everything with one command
bash run_full_stack.sh
```

This will:
1. ✅ Start the Python backend server
2. ✅ Install React dependencies (if needed)
3. ✅ Start the React development server
4. ✅ Open the app at `http://localhost:3000`

---

## 🎯 Individual Commands

### Start Backend Only

**Windows:**
```bash
start_backend.bat
```

**macOS/Linux:**
```bash
bash start_backend.sh
```

Backend will run at: `http://127.0.0.1:8000`

### Start Frontend Only

**Windows:**
```bash
start_frontend.bat
```

**macOS/Linux:**
```bash
bash start_frontend.sh
```

Frontend will run at: `http://localhost:3000`

---

## 📦 Manual Setup

### 1. Install Node Dependencies

```bash
cd client
npm install
```

### 2. Start Backend

```bash
cd server
python main.py
```

### 3. Start React Frontend

```bash
cd client
npm run dev
```

---

## 🏗️ Project Structure

```
MEDICAL ASSISTANT/
├── server/                 # Python FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   ├── routes/
│   ├── modules/
│   └── middleware/
│
├── client/                 # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── hooks/         # Custom hooks
│   │   ├── services/      # API services
│   │   ├── App.jsx        # Main component
│   │   └── index.css      # Global styles
│   ├── package.json
│   ├── vite.config.js
│   └── index.html
│
├── run_full_stack.bat     # Run everything (Windows)
├── run_full_stack.sh      # Run everything (macOS/Linux)
├── start_backend.bat      # Backend only (Windows)
├── start_backend.sh       # Backend only (macOS/Linux)
├── start_frontend.bat     # Frontend only (Windows)
└── start_frontend.sh      # Frontend only (macOS/Linux)
```

---

## ✨ New React Features

### Voice Input (FAST - No Server Wait!)
- Uses browser's native Web Speech API
- Instant transcript without server processing
- Works offline
- Click "Voice" tab in sidebar

### PDF Upload
- Drag & drop interface
- Multiple file support
- Real-time feedback
- Click "Documents" tab in sidebar

### Modern UI
- Responsive design
- Professional color scheme
- Smooth animations
- Collapsible sidebar

### Chat Features
- Real-time messaging
- Confidence scores
- Delete individual messages
- Export chat as JSON
- Session statistics

---

## 🔧 Available NPM Commands

```bash
cd client

# Development server with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Start (alias for dev)
npm start
```

---

## 🐛 Troubleshooting

### Port Already in Use

**Port 3000 (React):**
```bash
# Change port in vite.config.js
# server: {
#   port: 3001,  // Try a different port
# }
```

**Port 8000 (Backend):**
Find and kill the process:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

### Node Modules Issues
```bash
cd client
rm -rf node_modules package-lock.json
npm install
```

### Backend Connection Error
```bash
# Check if backend is running
http://127.0.0.1:8000

# Check server logs in the backend terminal
```

---

## 📊 Performance Improvements

| Feature | Old (Streamlit) | New (React) |
|---------|---|---|
| Voice to Text | 3-5 seconds server wait | Instant (browser API) |
| UI Load | Streamlit overhead | Lightning fast |
| File Upload | Standard | Drag & drop |
| Responsiveness | Moderate | Highly responsive |

---

## 🎨 Customization

### Change Theme Colors
Edit `client/tailwind.config.js`:
```js
colors: {
  medical: {
    500: '#0284c7',  // Change these
    600: '#0369a1',
  }
}
```

### Change Server URL
Edit `client/src/services/api.js`:
```js
const API_BASE_URL = 'http://your-server.com/api'
```

---

## 📞 Support

- **Backend Docs**: Check `server/README.md`
- **React Docs**: Check `client/README_REACT.md`
- **API Endpoints**: `http://127.0.0.1:8000/docs`

---

## ✅ All Set!

Your Medical Assistant app is now running with:
- ✅ Professional React UI
- ✅ Fast voice processing
- ✅ Modern features
- ✅ Responsive design

Start chatting! 🩺💬
