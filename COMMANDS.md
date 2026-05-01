# 🚀 QUICK RUN COMMANDS

## ✅ ONE COMMAND STARTUP (Recommended)

### Windows:
```bash
run_full_stack.bat
```

### macOS/Linux:
```bash
bash run_full_stack.sh
```

**What it does:**
- ✅ Starts backend server (port 8000)
- ✅ Installs React dependencies (if needed)
- ✅ Starts frontend server (port 3000)
- ✅ Opens browser automatically

---

## 🎯 INDIVIDUAL COMMANDS

### Start Backend Only

**Windows:**
```bash
start_backend.bat
```

**macOS/Linux:**
```bash
bash start_backend.sh
```

Backend runs at: `http://127.0.0.1:8000`

---

### Start Frontend Only

**Windows:**
```bash
start_frontend.bat
```

**macOS/Linux:**
```bash
bash start_frontend.sh
```

Frontend runs at: `http://localhost:3000`

---

## 📦 MANUAL SETUP

### Step 1: Install Node Packages
```bash
cd client
npm install
```

### Step 2: Start Backend
```bash
cd server
python main.py
```

### Step 3: Start Frontend (New Terminal)
```bash
cd client
npm run dev
```

---

## 🛠️ NPM COMMANDS

```bash
cd client

# Development with hot reload
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Start (alias for dev)
npm start
```

---

## 🐍 PYTHON COMMANDS

```bash
cd server

# Install dependencies
pip install -r requirements.txt

# Run backend server
python main.py

# Run with logging
python -u main.py
```

---

## 📍 URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs

---

## 🔍 VERIFY SETUP

```bash
# Check Node.js
node --version

# Check Python
python --version

# Check if ports are open
# Windows
netstat -ano | findstr :3000
netstat -ano | findstr :8000

# macOS/Linux
lsof -i :3000
lsof -i :8000
```

---

## ⚠️ TROUBLESHOOTING COMMANDS

### Reset Node Modules
```bash
cd client
rm -rf node_modules package-lock.json
npm install
```

### Kill Port 3000
```bash
# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:3000 | xargs kill -9
```

### Kill Port 8000
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -ti:8000 | xargs kill -9
```

---

## 🎉 THAT'S IT!

Choose your setup:
1. **Easy**: `run_full_stack.bat` ← Recommended
2. **Advanced**: Use individual start commands
3. **Manual**: Follow the manual setup steps

Then open: **http://localhost:3000**

---

**Ready? Pick one command above and get started! 🚀**
