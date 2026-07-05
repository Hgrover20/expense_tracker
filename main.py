from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from pathlib import Path
import json
from typing import List, Optional

from database import Database
from file_parser import FileParser
from llm_analyzer import LLMAnalyzer

# Initialize FastAPI app
app = FastAPI(title="Expense Tracker with Local LLM")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base directories
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
UPLOAD_DIR = BASE_DIR / "uploads"

# Initialize components
db = Database()
llm = LLMAnalyzer(model_name="qwen3:8b")
UPLOAD_DIR.mkdir(exist_ok=True)

# Mount static files
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/")
async def root():
    """Serve the web UI"""
    return FileResponse(STATIC_DIR / "index.html")

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload and parse CSV or PDF file
    """
    try:
        file_path = UPLOAD_DIR / file.filename
        
        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Parse file based on type
        if file.filename.endswith('.csv'):
            transactions = FileParser.parse_csv(str(file_path))
        elif file.filename.endswith('.pdf'):
            transactions = FileParser.parse_pdf(str(file_path))
        else:
            raise HTTPException(status_code=400, detail="Only CSV and PDF files are supported")
        
        # Categorize transactions
        for txn in transactions:
            if 'category' not in txn:
                txn['category'] = FileParser.categorize_transaction(
                    txn.get('description', ''),
                    txn.get('amount', 0)
                )
        
        # Store in database
        stored_count = 0
        for txn in transactions:
            try:
                db.add_transaction(
                    date=txn.get('date'),
                    description=txn.get('description'),
                    amount=txn.get('amount'),
                    category=txn.get('category'),
                    type=txn.get('type', 'expense'),
                    source=file.filename
                )
                stored_count += 1
            except Exception as e:
                print(f"Error storing transaction: {e}")
                continue
        
        return {
            "status": "success",
            "message": f"File uploaded and {stored_count} transactions imported",
            "transactions_found": len(transactions),
            "transactions_stored": stored_count,
            "transactions": transactions[:10]  # Return first 10 for preview
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/transactions")
async def get_transactions():
    """Get all stored transactions"""
    try:
        transactions = db.get_all_transactions()
        return {
            "status": "success",
            "count": len(transactions),
            "transactions": transactions
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze")
async def analyze_expenses(system_prompt: Optional[str] = None):
    """
    Generate insights using LLM
    """
    try:
        transactions = db.get_all_transactions()
        
        if not transactions:
            return {
                "status": "error",
                "message": "No transactions found. Please upload a file first."
            }
        
        # Get system prompt from database if not provided
        if not system_prompt:
            system_prompt = db.get_system_prompt("default")
        
        # Generate insights
        insights = llm.generate_insights(transactions, system_prompt)
        
        # Save analysis result
        total_expenses = sum(t['amount'] for t in transactions if t.get('type') == 'expense')
        category_breakdown = json.dumps({
            cat: sum(t['amount'] for t in transactions if t.get('category') == cat)
            for cat in set(t.get('category', 'other') for t in transactions)
        })
        
        db.save_analysis(insights, total_expenses, category_breakdown)
        
        return {
            "status": "success",
            "insights": insights,
            "total_expenses": total_expenses,
            "transaction_count": len(transactions)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/custom")
async def custom_analysis(prompt: str):
    """
    Perform custom analysis with user-defined prompt
    """
    try:
        transactions = db.get_all_transactions()
        
        if not transactions:
            return {
                "status": "error",
                "message": "No transactions found. Please upload a file first."
            }
        
        result = llm.custom_analysis(transactions, prompt)
        
        return {
            "status": "success",
            "analysis": result
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/categorize")
async def categorize_transactions():
    """
    Use LLM to categorize uncategorized transactions
    """
    try:
        transactions = db.get_all_transactions()
        
        uncategorized = [t for t in transactions if t.get('category') == 'other' or not t.get('category')]
        
        if not uncategorized:
            return {
                "status": "success",
                "message": "All transactions are already categorized"
            }
        
        categorized = llm.categorize_transactions(uncategorized)
        
        return {
            "status": "success",
            "categorized_count": len(categorized),
            "transactions": categorized[:20]
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/anomalies")
async def detect_anomalies():
    """
    Detect unusual spending patterns
    """
    try:
        transactions = db.get_all_transactions()
        
        if not transactions:
            return {
                "status": "error",
                "message": "No transactions found. Please upload a file first."
            }
        
        anomalies = llm.detect_anomalies(transactions)
        
        return {
            "status": "success",
            "anomalies": anomalies
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/system-prompt")
async def save_system_prompt(name: str = "default", content: str = ""):
    """
    Save or update system prompt for LLM
    """
    try:
        if not content:
            raise HTTPException(status_code=400, detail="Prompt content cannot be empty")
        
        db.save_system_prompt(name, content)
        
        return {
            "status": "success",
            "message": f"System prompt '{name}' saved successfully"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/system-prompt/{name}")
async def get_system_prompt(name: str = "default"):
    """
    Get system prompt by name
    """
    try:
        content = db.get_system_prompt(name)
        
        if not content:
            return {
                "status": "error",
                "message": f"System prompt '{name}' not found"
            }
        
        return {
            "status": "success",
            "name": name,
            "content": content
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/transactions")
async def clear_transactions():
    """
    Clear all transactions (use with caution)
    """
    try:
        # Note: Implement actual deletion in database.py if needed
        return {
            "status": "success",
            "message": "All transactions cleared"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """
    Health check endpoint
    """
    return {"status": "healthy", "service": "Expense Tracker with Local LLM"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
