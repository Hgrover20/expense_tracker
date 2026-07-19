# Configuration for Expense Tracker

# LLM Configuration
LLM_PROVIDER = "ollama"
LLM_MODEL_NAME = "qwen2.5:3b"
LLM_HOST = "http://localhost:11434"
LLM_TIMEOUT = 60  # seconds
LLM_NUM_CTX = 2048
LLM_NUM_PREDICT = 250
LLM_TEMPERATURE = 0.2
LLM_KEEP_ALIVE = "10m"

# Server Configuration
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000
DEBUG = False
CORS_ALLOWED_ORIGINS = ["*"]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_METHODS = ["*"]
CORS_ALLOWED_HEADERS = ["*"]

# Database Configuration
DB_PATH = "expenses.db"
UPLOAD_DIR = "uploads"

# Pagination
DEFAULT_PAGE_SIZE = 50

# Categorization
AUTO_CATEGORIZE = True
UNKNOWN_CATEGORY = "other"

# File Upload
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB
ALLOWED_EXTENSIONS = {".csv", ".pdf"}
