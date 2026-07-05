import csv
import re
from datetime import datetime
from typing import List, Dict, Tuple
from pypdf import PdfReader
import io

class FileParser:
    @staticmethod
    def parse_csv(file_path: str) -> List[Dict]:
        """Parse CSV file and extract transaction data"""
        try:
            transactions = []
            
            with open(file_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    transaction = FileParser._extract_transaction_data(row, "csv")
                    if transaction:
                        transactions.append(transaction)
            
            return transactions
        except Exception as e:
            print(f"Error parsing CSV: {e}")
            return []
    
    @staticmethod
    def parse_pdf(file_path: str) -> List[Dict]:
        """Parse PDF file (bank statements) and extract transaction data"""
        try:
            reader = PdfReader(file_path)
            text = ""
            
            for page in reader.pages:
                text += page.extract_text()
            
            transactions = FileParser._extract_from_text(text)
            return transactions
        except Exception as e:
            print(f"Error parsing PDF: {e}")
            return []
    
    @staticmethod
    def _extract_transaction_data(row, source: str) -> Dict:
        """Extract transaction data from a row"""
        transaction = {}
        
        # Try common column names
        date_cols = ['date', 'Date', 'DATE', 'transaction_date', 'Transaction Date']
        amount_cols = ['amount', 'Amount', 'AMOUNT', 'value', 'Value']
        desc_cols = ['description', 'Description', 'DESCRIPTION', 'narration', 'Narration']
        
        for col in date_cols:
            if col in row:
                transaction['date'] = str(row[col]).strip()
                break
        
        for col in amount_cols:
            if col in row:
                try:
                    transaction['amount'] = float(row[col].strip())
                except:
                    pass
                break
        
        for col in desc_cols:
            if col in row:
                transaction['description'] = str(row[col]).strip()
                break
        
        transaction['source'] = source
        transaction['type'] = 'expense' if transaction.get('amount', 0) > 0 else 'income'
        
        return transaction if 'date' in transaction and 'amount' in transaction else None
    
    @staticmethod
    def _extract_from_text(text: str) -> List[Dict]:
        """Extract transactions from unstructured text"""
        transactions = []
        
        # Pattern for date (DD/MM/YYYY or DD-MM-YYYY)
        # Followed by description and amount
        pattern = r'(\d{1,2}[-/]\d{1,2}[-/]\d{4})\s+(.+?)\s+(\d+\.?\d*)'
        
        matches = re.finditer(pattern, text)
        for match in matches:
            try:
                date_str = match.group(1)
                description = match.group(2).strip()
                amount = float(match.group(3))
                
                transaction = {
                    'date': date_str,
                    'description': description,
                    'amount': amount,
                    'source': 'pdf',
                    'type': 'expense'
                }
                transactions.append(transaction)
            except:
                continue
        
        return transactions
    
    @staticmethod
    def categorize_transaction(description: str, amount: float) -> str:
        """Auto-categorize transaction based on description"""
        description_lower = description.lower()
        
        categories = {
            'food': ['food', 'restaurant', 'cafe', 'pizza', 'burger', 'groceries', 'supermarket'],
            'transport': ['uber', 'taxi', 'auto', 'bus', 'metro', 'fuel', 'petrol', 'diesel'],
            'entertainment': ['movie', 'cinema', 'game', 'spotify', 'netflix', 'amazon', 'prime'],
            'utilities': ['electricity', 'water', 'internet', 'phone', 'mobile'],
            'health': ['hospital', 'doctor', 'medicine', 'pharmacy', 'clinic', 'health'],
            'shopping': ['amazon', 'flipkart', 'mall', 'store', 'shop', 'clothing'],
            'transfer': ['transfer', 'to account', 'sent to'],
        }
        
        for category, keywords in categories.items():
            if any(keyword in description_lower for keyword in keywords):
                return category
        
        return 'other'
