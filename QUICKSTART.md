# 🚀 Quick Start Guide

## 5-Minute Setup

### Step 1: Install Ollama (5 min)
1. Download Ollama from https://ollama.ai
2. Install and run it
3. Pull the Qwen2.5 3B model:
   ```bash
   ollama pull qwen2.5:3b
   ```

### Step 2: Set Up Python Environment (2 min)

**Windows:**
```bash
double-click setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Step 3: Start the Server (1 min)

```bash
# Activate virtual environment (if not already active)
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

# Run the server
python main.py
```

### Step 4: Open Web Interface

Navigate to: **http://localhost:8000**

## That's it! 🎉

You can now:
- Upload bank/UPI statements (CSV or PDF)
- Get AI-powered expense insights
- Analyze spending patterns
- Customize how the AI analyzes your expenses

---

## Common Tasks

### Upload a File
1. Click "Upload" tab
2. Drag and drop CSV or PDF file
3. System automatically parses and stores transactions

### Generate Insights
1. Go to "Analysis" tab
2. Click "Generate Insights"
3. Wait for LLM to analyze (5-30 seconds)
4. Read detailed insights about your spending

### Ask Custom Questions
1. Go to "Analysis" tab
2. In "Custom Analysis" section, type your question
3. Examples:
   - "What are my top 5 spending categories?"
   - "Which transactions seem unusual?"
   - "How can I save more money?"

### Customize AI Behavior
1. Go to "Settings" tab
2. Edit the "Default System Prompt"
3. Save and use it for future analyses

---

## Troubleshooting

### ❌ "Backend not running"
- Make sure you ran `python main.py`
- Check if the terminal shows any errors
- Verify no other app is using port 8000

### ❌ "Model not found" or "Connection refused"
- Start Ollama: `ollama serve`
- Verify model is installed: `ollama list`
- If not installed: `ollama pull qwen2.5:3b`

### ❌ "ModuleNotFoundError: No module named 'fastapi'"
- Rerun: `pip install -r requirements.txt`
- Or run setup script again

### ❌ "Port 8000 already in use"
- Edit `main.py` and change port from 8000 to another port (e.g., 8001)
- Or kill the process using that port

---

## File Format Guide

### CSV Files
Your CSV should have columns like:
```
date, description, amount
2024-01-15, Coffee Shop, 150.00
2024-01-15, Uber Ride, 250.00
```

### PDF Files
Bank PDFs typically work as-is. The system extracts:
- Transaction dates
- Descriptions/Narrations
- Amounts

---

## Tips for Best Results

✅ **Do:**
- Upload multiple months of data for better patterns
- Use descriptive transaction descriptions
- Keep consistent date formats
- Use custom prompts for specific analysis

❌ **Don't:**
- Upload very large PDFs (>100MB)
- Expect 100% accuracy in categorization
- Rely solely on anomaly detection for fraud detection
- Share your expense files with anyone

---

## Next Steps

1. **Explore Features**: Check out all tabs in the Web UI
2. **Customize Prompts**: Modify system prompt for different analysis types
3. **Regular Updates**: Upload statements regularly to track trends
4. **Backup Data**: Copy the `expenses.db` file for backups

---

## Need Help?

1. Check the README.md for detailed documentation
2. Review the troubleshooting section above
3. Check browser console (F12) for errors
4. Check terminal for server logs

---

Enjoy tracking your expenses! 💰
