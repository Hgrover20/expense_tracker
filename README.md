# 💰 Expense Tracker with Local LLM

An intelligent expense tracking application that uses a local LLM (Qwen3 8B) to analyze bank and UPI statements, providing AI-powered insights without any cloud dependencies.

## Features

✨ **Key Capabilities:**
- 📤 **File Upload**: Support for CSV and PDF bank/UPI statements
- 🤖 **Local LLM Integration**: Uses Qwen3 8B running locally via Ollama
- 💡 **AI-Powered Insights**: Automatic expense analysis and pattern detection
- 🏷️ **Smart Categorization**: Auto-categorize transactions with machine learning
- 🔍 **Anomaly Detection**: Identify unusual spending patterns
- ⚙️ **Custom Prompts**: Control LLM behavior with custom system prompts
- 💾 **Local Storage**: All data stored locally in SQLite (no cloud, no database)
- 🎨 **Web UI**: Beautiful, responsive interface for easy access

## Project Structure

```
expense_tracker/
├── main.py                 # FastAPI backend server
├── database.py            # SQLite database management
├── file_parser.py         # CSV/PDF parsing utilities
├── llm_analyzer.py        # LLM integration & analysis
├── requirements.txt       # Python dependencies
├── expenses.db           # Local SQLite database (created on first run)
├── uploads/              # Uploaded files directory
└── static/               # Frontend files
    ├── index.html        # Web UI
    ├── style.css         # Styling
    └── script.js         # Frontend logic
```

## Prerequisites

1. **Python 3.13.2+**
2. **Ollama** (for running local LLM)
   - Download from: https://ollama.ai
   - Pull Qwen3 8B: `ollama pull qwen3:8b`
3. **Qwen3 8B Model** (pulled via Ollama)

## Installation

### 1. Set Up Python Environment

```bash
# Navigate to project directory
cd e:\HIMANSHU\Agentic_AI\expense_tracker

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Ollama

```bash
# Download and install Ollama from https://ollama.ai

# Pull Qwen3 8B model
ollama pull qwen3:8b

# Start Ollama (it runs as a background service on port 11434)
# On Windows: Run Ollama application
# On Mac/Linux: ollama serve
```

### 4. Verify Ollama is Running

```bash
# Test if Ollama is accessible
curl http://localhost:11434/api/tags
```

## Usage

### 1. Start the Backend Server

```bash
python main.py
```

The server will start on `http://localhost:8000`

### 2. Access the Web Interface

Open your browser and go to: `http://localhost:8000`

### 3. Upload Your Bank Statement

- Click the "Upload" tab
- Drag and drop your CSV or PDF file
- The system will parse and store the transactions

### 4. Analyze Your Expenses

**Quick Analysis:**
- **Generate Insights**: Get AI-powered analysis of your spending patterns
- **Detect Anomalies**: Find unusual or suspicious transactions
- **Auto-Categorize**: Automatically categorize transactions

**Custom Analysis:**
- Enter your own questions about your expenses
- Get tailored analysis from the LLM

### 5. Customize System Prompts

In the Settings tab, customize the system prompt to control how the LLM analyzes your expenses.

## API Endpoints

### File Management
- `POST /upload` - Upload CSV or PDF file
- `GET /transactions` - Get all transactions
- `DELETE /transactions` - Clear all transactions

### Analysis
- `POST /analyze` - Generate insights using default system prompt
- `POST /analyze/custom` - Perform custom analysis
- `POST /analyze/categorize` - Auto-categorize transactions
- `POST /analyze/anomalies` - Detect anomalies

### System Prompts
- `POST /system-prompt` - Save/update system prompt
- `GET /system-prompt/{name}` - Get system prompt

### Health
- `GET /health` - Health check

## File Format Support

### CSV Format
Expected columns:
```
date, description, amount
2024-01-15, Groceries, 500.00
2024-01-15, Uber Ride, 250.00
```

### PDF Format
The system will attempt to parse bank statements in standard PDF format. Transactions should contain:
- Date (DD/MM/YYYY or DD-MM-YYYY)
- Description/Narration
- Amount

## Database Schema

### transactions table
```sql
- id: INTEGER (PRIMARY KEY)
- date: TEXT
- description: TEXT
- amount: REAL
- category: TEXT (food, transport, entertainment, etc.)
- type: TEXT (expense, income)
- source: TEXT (filename)
- created_at: TIMESTAMP
```

### analysis_results table
```sql
- id: INTEGER (PRIMARY KEY)
- analysis_date: TEXT
- insights: TEXT
- total_expenses: REAL
- category_breakdown: TEXT
- created_at: TIMESTAMP
```

### system_prompts table
```sql
- id: INTEGER (PRIMARY KEY)
- name: TEXT (UNIQUE)
- content: TEXT
- created_at: TIMESTAMP
- updated_at: TIMESTAMP
```

## Customization

### Adding New Categories

Edit `file_parser.py` in the `categorize_transaction()` method:

```python
categories = {
    'food': ['food', 'restaurant', 'cafe', 'pizza'],
    'your_category': ['keyword1', 'keyword2'],
}
```

### Changing the LLM Model

In `llm_analyzer.py`, change the model initialization:

```python
def __init__(self, model_name: str = "qwen3:8b"):
    # Change to any other model available in Ollama
    self.model_name = "mistral:7b"  # or any other model
```

Available Ollama models:
- `qwen3:8b` (recommended for this project)
- `mistral:7b`
- `llama2:7b`
- `neural-chat:7b`

### Custom System Prompts

You can set custom system prompts through the Web UI or via API:

```python
import requests

prompt = """You are a budget optimization expert. Analyze spending and provide:
1. Areas to cut expenses
2. Savings opportunities
3. Budget recommendations"""

requests.post(
    'http://localhost:8000/system-prompt',
    params={'name': 'budget_optimizer', 'content': prompt}
)
```

## Example Workflow

1. **Export from Bank**: Get CSV/PDF from your bank's portal
2. **Upload**: Drag and drop the file in the Web UI
3. **Review**: Check parsed transactions in the Transactions tab
4. **Analyze**: Click "Generate Insights" for AI analysis
5. **Customize**: Modify system prompt in Settings for different analysis types
6. **Export**: Save insights for your records

## Troubleshooting

### "Ollama is not running"
```bash
# Make sure Ollama service is running
ollama serve
```

### "Model not found"
```bash
# Pull the required model
ollama pull qwen3:8b
```

### "ModuleNotFoundError"
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Port already in use
Change port in `main.py`:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Change port here
```

## Technical Details

### Architecture
- **Backend**: FastAPI (Python web framework)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Database**: SQLite (local file-based)
- **LLM**: Ollama + Qwen3 8B (local inference)
- **File Parsing**: PyPDF, Pandas

### Data Privacy
✅ All data is processed locally
✅ No cloud uploads or external API calls
✅ No internet connectivity required (after model download)
✅ Complete control over your financial data

### Performance
- LLM inference time: 5-30 seconds per analysis (depending on transaction volume)
- File parsing: <1 second for typical statements
- Web UI: Instant response for navigation

## Future Enhancements

- [ ] Multiple user accounts
- [ ] Budget goal tracking
- [ ] Monthly/yearly reports
- [ ] Spending trends visualization
- [ ] Export analysis as PDF
- [ ] Integration with more file formats
- [ ] Mobile app version

## License

MIT License - Feel free to use and modify

## Support

For issues or questions:
1. Check the troubleshooting section
2. Verify Ollama is running and has the model
3. Check browser console for errors (F12)
4. Review application logs

---

Built with ❤️ for privacy-conscious expense tracking
