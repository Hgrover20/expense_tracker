# ✅ Setup Checklist

Use this checklist to ensure your Expense Tracker is properly set up and running.

## Pre-Installation Checklist

- [ ] Python 3.13.2+ installed (check: `python --version`)
- [ ] Git installed (optional but recommended)
- [ ] ~5 GB disk space available for Ollama and models
- [ ] Stable internet connection for downloading Ollama and models

## Installation Steps

### Step 1: Install Ollama
- [ ] Download Ollama from https://ollama.ai
- [ ] Complete Ollama installation
- [ ] Restart computer if prompted
- [ ] Verify Ollama is installed: `ollama --version`

### Step 2: Download Qwen2.5 3B Model
- [ ] Open terminal/command prompt
- [ ] Run: `ollama pull qwen2.5:3b`
- [ ] Wait for download to complete (~4GB)
- [ ] Verify model is installed: `ollama list`

### Step 3: Clone/Extract Project
- [ ] Extract the project folder to your desired location
- [ ] Navigate to: `e:\HIMANSHU\Agentic_AI\expense_tracker`

### Step 4: Set Up Python Environment

**Windows:**
- [ ] Double-click `setup.bat`
- [ ] Wait for setup to complete
- [ ] Close the terminal when done

**Mac/Linux:**
- [ ] Open terminal in project directory
- [ ] Run: `chmod +x setup.sh`
- [ ] Run: `./setup.sh`
- [ ] Wait for setup to complete

### Step 5: Manual Setup (If scripts don't work)
- [ ] Create virtual environment: `python -m venv venv`
- [ ] Activate virtual environment:
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
- [ ] Install dependencies: `pip install -r requirements.txt`

## Pre-Launch Verification

### Check Python Dependencies
```bash
# Verify all packages are installed
pip list | grep -E "fastapi|uvicorn|pandas|pypdf|ollama"
```
- [ ] All packages listed above are installed

### Check Ollama Service
```bash
# Check if Ollama is running and accessible
curl http://localhost:11434/api/tags
```
- [ ] Ollama is running (returns a response)
- [ ] Qwen3 8B model is in the list

### Check Port Availability
```bash
# Make sure port 8000 is available
# Windows: netstat -ano | findstr :8000
# Mac/Linux: lsof -i :8000
```
- [ ] Port 8000 is available (no output means it's free)

## Startup Sequence

### 1. Start Ollama Service
**Windows:**
- [ ] Ollama application is running in taskbar
- [ ] OR run in terminal: `ollama serve`

**Mac/Linux:**
- [ ] Open terminal
- [ ] Run: `ollama serve`
- [ ] Keep the terminal open

### 2. Start the Backend Server
- [ ] Activate virtual environment (if not already)
  - Windows: `venv\Scripts\activate`
  - Mac/Linux: `source venv/bin/activate`
- [ ] Run: `python main.py`
- [ ] Verify output shows: `INFO: Started server process [xxxxx]`
- [ ] Verify: `Uvicorn running on http://0.0.0.0:8000`

### 3. Open Web Interface
- [ ] Open web browser
- [ ] Navigate to: `http://localhost:8000`
- [ ] Verify page loads with "Expense Tracker with Local LLM" title
- [ ] Check "Status" shows: ✅ Running

## First-Time Usage

### Test File Upload
- [ ] Sample file exists: `sample_transactions.csv`
- [ ] Go to "Upload" tab
- [ ] Upload `sample_transactions.csv`
- [ ] Verify transactions appear in "Transactions" tab
- [ ] Verify at least 5 transactions are listed

### Test Analysis
- [ ] Go to "Analysis" tab
- [ ] Click "Generate Insights"
- [ ] Wait for LLM to process (5-30 seconds)
- [ ] Verify you get insight output with analysis

### Test Custom Prompt
- [ ] Go to "Settings" tab
- [ ] Scroll to "Default System Prompt"
- [ ] Verify default prompt is shown
- [ ] (Optional) Modify the prompt
- [ ] Click "Save Default Prompt"
- [ ] Verify success message appears

## Troubleshooting Checklist

If something doesn't work:

### Server Won't Start
- [ ] Check if Python is in PATH: `python --version`
- [ ] Check if venv is activated (prompt shows `(venv)`)
- [ ] Check if port 8000 is free
- [ ] Check terminal for specific error messages
- [ ] Try changing port in `main.py` if 8000 is in use

### LLM Not Responding
- [ ] Check if Ollama is running: `curl http://localhost:11434/api/tags`
- [ ] Check if Qwen2.5 3B is installed: `ollama list`
- [ ] If not installed: `ollama pull qwen2.5:3b`
- [ ] Restart Ollama service
- [ ] Restart the backend server

### Web UI Not Loading
- [ ] Check if backend server is running
- [ ] Try hard refresh: `Ctrl+Shift+R` (or `Cmd+Shift+R` on Mac)
- [ ] Check browser console for errors: `F12`
- [ ] Try different browser (Chrome, Firefox, Edge)

### File Upload Fails
- [ ] Verify file is CSV or PDF format
- [ ] Check file size is < 50MB
- [ ] Try with `sample_transactions.csv` first
- [ ] Check `uploads/` folder exists
- [ ] Check permissions are correct

### Slow Performance
- [ ] Close unnecessary applications
- [ ] Check if other services are using CPU
- [ ] If Ollama is slow, it might need more system resources
- [ ] LLM inference takes 5-30 seconds - this is normal

## Daily Usage Checklist

Before each session:
- [ ] Start Ollama service: `ollama serve`
- [ ] Start backend server: `python main.py`
- [ ] Open browser to `http://localhost:8000`
- [ ] Verify status shows ✅ Running

For file uploads:
- [ ] Export statement from bank/UPI app
- [ ] Save as CSV or PDF
- [ ] Upload via web UI
- [ ] Wait for processing to complete

For analysis:
- [ ] Review uploaded transactions
- [ ] Click "Generate Insights"
- [ ] (Optional) Modify system prompt for different analysis
- [ ] Review and save insights

## Backup Checklist

To protect your data:
- [ ] Regularly backup `expenses.db` file
- [ ] Save important insights to separate files
- [ ] Keep CSV/PDF backups of uploaded statements
- [ ] Export data periodically

## Deactivation Checklist

When closing the application:
- [ ] Close web browser tab
- [ ] Stop backend server: `Ctrl+C` in terminal
- [ ] Stop Ollama service: `Ctrl+C` or close application
- [ ] (Optional) Close terminal windows

## Notes

- **First Run**: First analysis might take longer as LLM loads model into memory
- **Multiple Users**: Each user needs their own expenses.db file
- **Data Privacy**: All data stays on your machine - never sent to cloud
- **Performance**: On first run of LLM for the session, it loads model (5-10 seconds)
- **Updates**: Check GitHub for updates and improvements

## Support Resources

- 📖 README.md - Full documentation
- ⚡ QUICKSTART.md - Quick setup guide
- 💡 SYSTEM_PROMPTS.md - Guide for creating custom prompts
- 📝 sample_transactions.csv - Example file for testing

## Success Indicators

You've successfully set up if:
✅ Backend server starts without errors
✅ Web page loads at http://localhost:8000
✅ Status shows "✅ Running"
✅ You can upload sample_transactions.csv
✅ You can generate insights
✅ Analysis results appear in < 30 seconds

---

**Congratulations!** Your Expense Tracker is ready to use. Start uploading your bank statements and let AI analyze your spending! 🎉
