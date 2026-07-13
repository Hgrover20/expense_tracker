# 📋 Project Summary

## Project: Expense Tracker with Local LLM

A complete, self-contained expense tracking application using Qwen2 8B local LLM for AI-powered financial analysis.

---

## 🎯 What You Get

### Core Features
✅ Upload bank/UPI statements (CSV or PDF)
✅ Automatic transaction parsing and categorization
✅ AI-powered expense analysis using local Qwen2.5 3B
✅ Pattern detection and anomaly identification
✅ Custom system prompts for controlled LLM output
✅ Local SQLite database (no cloud, no external DB)
✅ Beautiful web interface
✅ Complete privacy - everything runs locally

### Tech Stack
- **Backend**: Python 3.13.2+, FastAPI, Uvicorn
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite (local file-based)
- **LLM**: Qwen2 8B via Ollama
- **File Parsing**: PyPDF, Pandas

---

## 📁 Project Structure

```
expense_tracker/
│
├── Backend Files
│   ├── main.py                    # FastAPI server & API endpoints
│   ├── database.py                # SQLite database management
│   ├── file_parser.py             # CSV/PDF parsing
│   ├── llm_analyzer.py            # LLM integration & analysis
│   └── config.py                  # Configuration settings
│
├── Frontend Files (static/)
│   ├── index.html                 # Web UI
│   ├── style.css                  # Styling & responsiveness
│   └── script.js                  # Frontend logic
│
├── Documentation
│   ├── README.md                  # Complete documentation
│   ├── QUICKSTART.md              # 5-minute setup guide
│   ├── SETUP_CHECKLIST.md         # Step-by-step verification
│   └── SYSTEM_PROMPTS.md          # Custom prompt examples
│
├── Setup Scripts
│   ├── setup.bat                  # Windows setup automation
│   └── setup.sh                   # Mac/Linux setup automation
│
├── Configuration & Metadata
│   ├── requirements.txt           # Python dependencies
│   ├── .gitignore                 # Git ignore patterns
│   └── sample_transactions.csv    # Test data
│
└── Runtime Files (created on first run)
    ├── expenses.db                # SQLite database
    └── uploads/                   # Uploaded files
```

---

## 📦 File Descriptions

### Backend Core Files

#### `main.py` (FastAPI Server)
- **Purpose**: Main application server
- **Responsibilities**: 
  - API endpoints for file upload and analysis
  - Handles HTTP requests from frontend
  - Orchestrates file parsing, database, and LLM
  - Serves static frontend files
- **Key Endpoints**:
  - `POST /upload` - Upload and parse files
  - `POST /analyze` - Generate insights
  - `POST /analyze/custom` - Custom analysis
  - `POST /analyze/categorize` - Auto-categorize
  - `POST /analyze/anomalies` - Detect anomalies
  - `POST /system-prompt` - Save custom prompts

#### `database.py` (SQLite Management)
- **Purpose**: Local data persistence
- **Responsibilities**:
  - Create and manage SQLite database
  - Store transactions
  - Save analysis results
  - Manage system prompts
- **Tables**:
  - `transactions` - Individual expenses
  - `analysis_results` - Analysis history
  - `system_prompts` - Custom prompts library

#### `file_parser.py` (File Processing)
- **Purpose**: Parse uploaded files
- **Responsibilities**:
  - Read CSV files with flexible column detection
  - Extract text from PDF documents
  - Parse unstructured text for transactions
  - Auto-categorize based on description
  - Detect transaction types (expense/income)
- **Smart Features**:
  - Handles various CSV column names
  - Pattern matching for PDF text
  - Intelligent categorization using keywords

#### `llm_analyzer.py` (LLM Integration)
- **Purpose**: AI-powered analysis
- **Responsibilities**:
  - Connect to local Ollama service
  - Generate insights from transactions
  - Categorize uncategorized transactions
  - Detect spending anomalies
  - Support custom user prompts
- **Methods**:
  - `generate_insights()` - Full analysis with system prompt
  - `categorize_transactions()` - AI-based categorization
  - `detect_anomalies()` - Find unusual spending
  - `custom_analysis()` - User-defined analysis

#### `config.py` (Configuration)
- **Purpose**: Centralized configuration
- **Variables**:
  - LLM model and endpoint settings
  - Server host/port configuration
  - Database path and file upload settings
  - Default categories and other constants

### Frontend Files

#### `index.html` (Web UI)
- **Purpose**: User interface
- **Sections**:
  - Upload tab - File upload interface
  - Transactions tab - View all transactions
  - Analysis tab - Run various analyses
  - Settings tab - Customize system prompts
- **Features**:
  - Responsive design for mobile/desktop
  - Real-time filtering and search
  - Progress indicators for async operations

#### `style.css` (Styling)
- **Purpose**: Visual design and layout
- **Features**:
  - Modern gradient background
  - Card-based layout
  - Responsive grid system
  - Smooth animations and transitions
  - Dark/light color scheme
  - Mobile-optimized responsive design

#### `script.js` (Frontend Logic)
- **Purpose**: Client-side interactivity
- **Features**:
  - File drag-and-drop handling
  - API communication with backend
  - Tab switching
  - Transaction filtering and search
  - Analysis result display
  - System prompt management

### Documentation Files

#### `README.md` (Complete Guide)
- Installation instructions
- Usage guide with screenshots
- API reference
- Database schema
- Troubleshooting guide
- Customization examples

#### `QUICKSTART.md` (Quick Setup)
- 5-minute setup summary
- Common tasks guide
- Troubleshooting quick reference
- File format examples

#### `SETUP_CHECKLIST.md` (Verification)
- Pre-installation checklist
- Step-by-step setup verification
- Troubleshooting checklist
- Daily usage checklist
- Backup procedures

#### `SYSTEM_PROMPTS.md` (AI Customization)
- 10+ example system prompts
- Prompt creation template
- Advanced prompt techniques
- Prompt testing guide
- Tips for effective prompts

### Setup & Configuration

#### `setup.bat` (Windows Automation)
- Automated Python environment setup for Windows
- Virtual environment creation
- Dependency installation
- Pre-flight checks

#### `setup.sh` (Linux/Mac Automation)
- Automated Python environment setup for Unix-like systems
- Virtual environment creation
- Dependency installation
- Pre-flight checks

#### `requirements.txt` (Dependencies)
```
fastapi==0.104.1          # Web framework
uvicorn==0.24.0           # ASGI server
python-multipart==0.0.6   # Form data parsing
pydantic==2.4.2           # Data validation
sqlite3                    # Database
ollama==0.0.21            # LLM client
pypdf==3.17.1             # PDF reading
pandas==2.1.3             # CSV parsing
python-dotenv==1.0.0      # Environment variables
aiofiles==23.2.1          # Async file handling
```

#### `.gitignore` (Git Configuration)
- Excludes virtual environments
- Excludes database files
- Excludes uploaded files
- Excludes IDE configurations
- Excludes Python cache files

#### `sample_transactions.csv` (Test Data)
- 30 sample transactions
- Various expense categories
- Real-world examples
- For testing without actual bank data

---

## 🚀 Getting Started

### Quickest Path (5 minutes)

1. **Install Ollama**
   ```bash
   # Download from https://ollama.ai
   ollama pull qwen2:8b
   ```

2. **Run Setup Script**
   ```bash
   # Windows: double-click setup.bat
   # Mac/Linux: chmod +x setup.sh && ./setup.sh
   ```

3. **Start Server**
   ```bash
   python main.py
   ```

4. **Open Browser**
   ```
   http://localhost:8000
   ```

### Detailed Setup
See `QUICKSTART.md` or `SETUP_CHECKLIST.md`

---

## 💾 Data Storage

### Local Storage Only
- **Database**: `expenses.db` (SQLite)
- **Uploaded Files**: `uploads/` folder
- **Configuration**: In-memory + database

### Data Structure
```
expenses.db
├── transactions (30+ fields)
│   ├── id, date, description, amount
│   ├── category, type, source
│   └── created_at timestamp
│
├── analysis_results (history)
│   ├── id, analysis_date, insights
│   ├── total_expenses, category_breakdown
│   └── created_at timestamp
│
└── system_prompts (custom)
    ├── id, name, content
    └── created_at, updated_at timestamps
```

---

## 🔌 API Reference

### Upload & Management
```
POST   /upload              # Upload CSV/PDF
GET    /transactions        # Get all transactions
DELETE /transactions        # Clear all transactions
GET    /health              # Health check
```

### Analysis
```
POST   /analyze             # Full analysis with system prompt
POST   /analyze/custom      # Custom user-defined analysis
POST   /analyze/categorize  # Auto-categorize transactions
POST   /analyze/anomalies   # Detect unusual spending
```

### System Prompts
```
POST   /system-prompt       # Save/update prompt
GET    /system-prompt/{name} # Get prompt by name
```

---

## 🎨 Customization Options

### 1. Change LLM Model
Edit `llm_analyzer.py`:
```python
self.model_name = "mistral:7b"  # or any Ollama model
```

### 2. Add Categories
Edit `file_parser.py` `categorize_transaction()`:
```python
'your_category': ['keyword1', 'keyword2']
```

### 3. Customize System Prompts
Via Web UI Settings tab or edit default in `llm_analyzer.py`

### 4. Change Server Port
Edit `main.py`:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)
```

### 5. Modify UI
Edit `static/index.html`, `style.css`, `script.js`

---

## 🔒 Privacy & Security

✅ **Complete Local Processing**
- No cloud uploads
- No API calls to external services
- No data transmission
- All processing on your machine

✅ **Data Control**
- You own all your financial data
- Easy to backup (copy expenses.db)
- Easy to delete (remove expenses.db)
- No tracking or analytics

✅ **Offline Capability**
- Works completely offline after initial LLM download
- No internet required for analysis
- No connectivity required for normal operation

---

## 📊 Use Cases

1. **Personal Finance Management**
   - Track where money goes
   - Identify spending patterns
   - Find optimization opportunities

2. **Budget Planning**
   - Analyze spending by category
   - Set and track budget goals
   - Identify areas to cut expenses

3. **Investment Planning**
   - Calculate potential savings
   - Assess investment capacity
   - Build wealth strategy

4. **Tax Preparation**
   - Categorize deductible expenses
   - Identify tax opportunities
   - Organize documentation

5. **Fraud Detection**
   - Identify suspicious transactions
   - Detect unusual patterns
   - Monitor account security

6. **Financial Education**
   - Learn spending habits
   - Understand expense patterns
   - Improve financial literacy

---

## 🛠️ Maintenance

### Regular Tasks
- Backup `expenses.db` weekly
- Update system prompts as needed
- Clean old uploads from `uploads/` folder
- Review analysis results periodically

### Troubleshooting
- See SETUP_CHECKLIST.md troubleshooting section
- Check browser console (F12) for errors
- Review terminal output for server errors
- Verify Ollama is running and accessible

### Updates
- Check for new Ollama models: `ollama list`
- Update Python packages: `pip install --upgrade -r requirements.txt`
- Monitor GitHub for improvements and bug fixes

---

## 📞 Support

### Documentation
- 📖 README.md - Full documentation
- ⚡ QUICKSTART.md - Quick setup
- ✅ SETUP_CHECKLIST.md - Verification
- 💡 SYSTEM_PROMPTS.md - AI customization

### Common Issues
See SETUP_CHECKLIST.md troubleshooting section

### System Requirements
- Python 3.13.2+
- 8GB RAM recommended
- ~5GB disk for Ollama + model
- Windows 10+, macOS 10.13+, or Linux

---

## 📈 Project Growth

### Currently Included
✅ File upload (CSV/PDF)
✅ Transaction parsing
✅ Auto-categorization
✅ Local LLM analysis
✅ Custom system prompts
✅ Web UI
✅ SQLite database

### Future Enhancements
- [ ] Multiple user accounts
- [ ] Budget tracking & goals
- [ ] Monthly/yearly reports
- [ ] Visualization charts
- [ ] PDF export
- [ ] Mobile app
- [ ] API authentication
- [ ] Data encryption

---

## 🎓 Learning Resources

This project demonstrates:
- FastAPI web framework
- SQLite database management
- File parsing (CSV, PDF)
- LLM integration with Ollama
- Frontend-backend communication
- RESTful API design
- Responsive web design
- Python best practices

---

## 📝 License

MIT License - Free to use and modify

---

## 🙏 Final Notes

### Privacy First
Your financial data never leaves your machine. Complete control over your information.

### Offline Operation
After downloading Qwen2.5 3B, everything works offline. Perfect for privacy-conscious users.

### Customizable AI
Control exactly how the AI analyzes your data using system prompts.

### No Tracking
No user tracking, analytics, or data collection. Your usage is private.

---

**Ready to get started?** Follow QUICKSTART.md or SETUP_CHECKLIST.md! 🚀

Built with ❤️ for privacy-conscious expense tracking
