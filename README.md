# FastAPI Environment Oracle 🚀

A diagnostic utility designed to verify "Pure" Python 13 environments, validate pathing, and demonstrate secure secret management.

## 🛠️ Features
- **Environment Diagnostics:** Real-time verification of Python version and executable paths.
- **Secret Management:** Secure handling of API keys using `python-dotenv`.
- **Clean Architecture:** Zero-bloat setup (Anaconda-free) with 100% isolation.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.13
- A local virtual environment (`.venv`)

### 2. Environment Setup
The project uses a `.env` file for local secrets. To get started:
1. Copy the template: `cp .env.example .env` (or manually copy/paste)
2. Open `.env` and add your local configuration.

### 3. Installation
```powershell
pip install -r requirements.txt