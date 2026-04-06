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
uvicorn app.main:app --reload
```
### 4. Running with Docker (The "One-Click" Method)
This project is fully containerized for professional deployment. To run the entire environment (including secret management and live-reload volumes) with a single command:
1. Build and Start:
```powershell
docker-compose up --build
```
2. Access: The Oracle will be live at: http://localhost:8000/