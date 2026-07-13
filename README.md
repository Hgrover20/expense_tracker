# Expense Tracker with Local LLM

A simple local expense tracker that reads CSV/PDF transactions, stores them in SQLite, and uses a local LLM for smart expense analysis.

## Quick commands

```cmd 
cd E\expense_tracker (Make sure to change as per your file path)
venv\Scripts\activate
pip install -r requirements.txt
ollama pull qwen2.5:3b
python main.py
```

## Quick setup

1. Open PowerShell and go to the app folder:

```powershell
cd your folder path
```

2. Activate the virtual environment:

```powershell
venv\Scripts\activate
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Install Ollama and download a model:

```powershell
ollama pull qwen2.5:3b
```

5. Make sure Ollama is running.

## Run the app

```powershell
python main.py
```

Then open this in your browser:

http://127.0.0.1:8000

## What this project includes

- Upload and parse CSV/PDF bank or UPI statements
- Store transactions locally in `expenses.db`
- Auto-categorize expenses by description
- Use a local Ollama LLM to generate spending insights and detect anomalies
- Support custom analysis prompts
- Simple browser interface in `static/`

## How to use it

- Upload a CSV or PDF file on the web page
- The app parses transactions and stores them locally
- View saved transactions in the transactions tab
- Run analysis for insights and anomaly detection
- Use custom analysis to ask questions about your spending

## Files you should know

- `main.py` – web server and API routes
- `database.py` – SQLite storage for transactions and prompts
- `file_parser.py` – parse uploaded CSV/PDF files
- `llm_analyzer.py` – local LLM integration for analysis
- `config.py` – app settings and model configuration
- `requirements.txt` – Python dependencies
- `static/index.html` – browser UI
- `static/style.css` – UI styling
- `static/script.js` – browser behavior
- `uploads/` – uploaded files
- `expenses.db` – created automatically after first run

## API routes

- `POST /upload` – upload CSV or PDF
- `GET /transactions` – get saved transactions
- `DELETE /transactions` – clear all transactions
- `POST /analyze` – run default AI analysis
- `POST /analyze/custom` – run a custom prompt
- `POST /analyze/categorize` – categorize uncategorized items
- `POST /analyze/anomalies` – find unusual spending
- `POST /system-prompt` – save or update a prompt
- `GET /system-prompt/{name}` – get a saved prompt
- `GET /health` – check the app status

## Change the LLM model

Edit `config.py`:

```python
LLM_PROVIDER = "ollama"
LLM_MODEL_NAME = "qwen2.5:3b"
```

Use a smaller local model if your computer is CPU-only.

## Add new categories

Edit `file_parser.py` in `categorize_transaction()` and add new keyword lists.

## Troubleshooting

- Use `http://127.0.0.1:8000` in the browser
- If analysis fails, make sure Ollama is running on `http://localhost:11434`
- If the app cannot start, check that required Python packages are installed

## Important notes

- Data is stored locally only
- No cloud uploads
- Ollama must be installed separately
- Choose CPU-friendly models for local use

# Make sure Ollama service is running
ollama serve
```

### "Model not found"
```bash
# Pull the required model
ollama pull qwen2.5:3b
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

