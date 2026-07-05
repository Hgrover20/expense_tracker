import sqlite3
import os
from datetime import datetime
from typing import List, Dict, Optional

class Database:
    def __init__(self, db_path: str = "expenses.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize database with required tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Transactions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                description TEXT,
                amount REAL NOT NULL,
                category TEXT,
                type TEXT,
                source TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Analysis results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analysis_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                analysis_date TEXT NOT NULL,
                insights TEXT,
                total_expenses REAL,
                category_breakdown TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # System prompts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS system_prompts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_transaction(self, date: str, description: str, amount: float, 
                       category: str = None, type: str = "expense", source: str = None) -> int:
        """Add a transaction to the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO transactions (date, description, amount, category, type, source)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, description, amount, category, type, source))
        
        transaction_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return transaction_id
    
    def get_all_transactions(self) -> List[Dict]:
        """Get all transactions"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
        transactions = [dict(row) for row in cursor.fetchall()]
        
        conn.close()
        return transactions
    
    def save_analysis(self, insights: str, total_expenses: float, category_breakdown: str):
        """Save analysis results"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO analysis_results (analysis_date, insights, total_expenses, category_breakdown)
            VALUES (?, ?, ?, ?)
        ''', (datetime.now().isoformat(), insights, total_expenses, category_breakdown))
        
        conn.commit()
        conn.close()
    
    def save_system_prompt(self, name: str, content: str):
        """Save or update system prompt"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO system_prompts (name, content, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
        ''', (name, content))
        
        conn.commit()
        conn.close()
    
    def get_system_prompt(self, name: str = "default") -> Optional[str]:
        """Get system prompt by name"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT content FROM system_prompts WHERE name = ?', (name,))
        result = cursor.fetchone()
        conn.close()
        
        return result[0] if result else None
