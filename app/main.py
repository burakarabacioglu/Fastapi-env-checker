import os
import sys
from datetime import datetime
from fastapi import FastAPI
from dotenv import load_dotenv

# Load variables from .env into the system environment
load_dotenv()

app = FastAPI(title="Environment Oracle")

@app.get("/")
def get_diagnostics():
    return {
        "timestamp": datetime.now().isoformat(),
        "python_info": {
            "version": sys.version,
            "executable": sys.executable
        },
        "env_vars": {
            "api_key_loaded": "API_KEY" in os.environ,
            "current_env": os.getenv("ENVIRONMENT", "Not Set"),
            "app_debug": os.getenv("APP_DEBUG", "False")
        }
    }