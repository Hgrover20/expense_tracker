from typing import List, Dict, Optional
import json

from llm.manager import LLMManager


class LLMAnalyzer:
    def __init__(self, model_name: str = "qwen2.5:3b"):
        self.model_name = model_name
        self.manager = LLMManager(model_name=self.model_name)
        
    def generate_insights(self, transactions: List[Dict], system_prompt: Optional[str] = None) -> str:
        """
        Generate insights from transaction data using local LLM
        """
        if not system_prompt:
            system_prompt = self._get_default_system_prompt()
        
        # Prepare transaction summary for the LLM
        transaction_summary = self._prepare_transaction_summary(transactions)
        
        user_message = f"""
Analyze the following expense transaction data and provide detailed insights:

{transaction_summary}

Based on this data, provide:
1. Total expenses and income breakdown
2. Top spending categories
3. Daily/weekly spending patterns
4. Areas where spending can be optimized
5. Financial health assessment
6. Specific recommendations for expense management
"""
        
        response_text = self.manager.generate_with_options(
            prompt=user_message,
            system=system_prompt,
            options={
                "num_ctx": self.manager.options.get("num_ctx"),
                "num_predict": self.manager.options.get("num_predict"),
                "temperature": self.manager.options.get("temperature"),
            },
        )
        
        return response_text
    
    def categorize_transactions(self, transactions: List[Dict]) -> List[Dict]:
        """
        Use LLM to intelligently categorize transactions
        """
        prompt = self._prepare_categorization_prompt(transactions)
        
        response_text = self.manager.generate_with_options(
            prompt=prompt,
            system="You are an expert financial analyzer. Categorize the following transactions accurately.",
            options={
                "num_ctx": self.manager.options.get("num_ctx"),
                "num_predict": self.manager.options.get("num_predict"),
                "temperature": 0.1,
            },
        )
        
        return self._parse_categorization_response(response_text, transactions)
    
    def detect_anomalies(self, transactions: List[Dict]) -> List[Dict]:
        """
        Detect unusual spending patterns or anomalies
        """
        prompt = f"""
Analyze these transactions and identify any unusual patterns or anomalies:

{json.dumps(transactions, indent=2)}

List any suspicious or unusual transactions with explanations.
"""
        
        response_text = self.manager.generate_with_options(
            prompt=prompt,
            system="You are a fraud detection expert. Identify anomalies in expense patterns.",
            options={
                "num_ctx": self.manager.options.get("num_ctx"),
                "num_predict": 180,
                "temperature": 0.1,
            },
        )
        
        return response_text
    
    def custom_analysis(self, transactions: List[Dict], custom_prompt: str) -> str:
        """
        Perform custom analysis based on user-defined prompt
        """
        transaction_summary = self._prepare_transaction_summary(transactions)
        
        full_prompt = f"""
Transaction Data:
{transaction_summary}

User Request:
{custom_prompt}
"""
        
        response_text = self.manager.generate_with_options(
            prompt=full_prompt,
            options={
                "num_ctx": self.manager.options.get("num_ctx"),
                "num_predict": self.manager.options.get("num_predict"),
                "temperature": 0.2,
            },
        )
        
        return response_text
    
    def _prepare_transaction_summary(self, transactions: List[Dict]) -> str:
        """Prepare a compact transaction summary for faster LLM analysis"""
        if not transactions:
            return "No transaction data available."

        summary = "Transaction Summary:\n"
        summary += "-" * 80 + "\n"

        total_expenses = 0
        total_income = 0
        category_totals = {}
        recent_items = []

        for txn in transactions[-20:]:
            recent_items.append(
                f"{txn.get('date', 'N/A')} | {txn.get('description', 'N/A')} | {txn.get('amount', 0)} | {txn.get('category', 'uncategorized')}"
            )

        for txn in transactions:
            amount = float(txn.get('amount', 0) or 0)
            if txn.get('type') == 'expense':
                total_expenses += amount
                category = txn.get('category', 'other')
                category_totals[category] = category_totals.get(category, 0) + amount
            else:
                total_income += amount

        summary += f"Transactions analyzed: {len(transactions)}\n"
        summary += f"Total expenses: {total_expenses}\n"
        summary += f"Total income: {total_income}\n"
        summary += "Top categories:\n"

        for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True)[:8]:
            summary += f"  - {category}: {total}\n"

        if recent_items:
            summary += "Recent transactions:\n"
            for item in recent_items:
                summary += f"  - {item}\n"

        return summary
    
    def _prepare_categorization_prompt(self, transactions: List[Dict]) -> str:
        """Prepare prompt for transaction categorization"""
        prompt = "Categorize these transactions into: Food, Transport, Entertainment, Utilities, Health, Shopping, Transfer, Other\n\n"
        
        for i, txn in enumerate(transactions, 1):
            prompt += f"{i}. {txn.get('description', 'Unknown')} - Amount: {txn.get('amount', 0)}\n"
        
        prompt += "\nRespond with a JSON array with 'id' and 'category' for each transaction."
        return prompt
    
    def _parse_categorization_response(self, response: str, transactions: List[Dict]) -> List[Dict]:
        """Parse LLM response for categorization"""
        # Try to extract JSON from response
        try:
            json_start = response.find('[')
            json_end = response.rfind(']') + 1
            json_str = response[json_start:json_end]
            categories = json.loads(json_str)
            
            for category_info in categories:
                idx = category_info.get('id', 1) - 1
                if idx < len(transactions):
                    transactions[idx]['category'] = category_info.get('category', 'other')
        except:
            pass
        
        return transactions
    
    def _get_default_system_prompt(self) -> str:
        """Return default system prompt for expense analysis"""
        return """You are an expert financial analyst specializing in personal expense management. 
Your role is to:
1. Analyze spending patterns and provide actionable insights
2. Identify areas of overspending
3. Suggest budget optimization strategies
4. Highlight positive spending habits
5. Provide specific, measurable recommendations

Be concise, data-driven, and focus on practical advice that can improve financial health."""
