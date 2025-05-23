# Sentiment Analyzer FastAPI App

## 📌 What it does
This FastAPI application analyzes the sentiment of a given piece of text (Positive, Negative, Neutral).

## 🚀 How to Run

### Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Using Docker
```bash
docker build -t sentiment-analyzer .
docker run -d -p 8000:8000 sentiment-analyzer
http://localhost:8000  # open in browser 
```

## ⚙️ Configuration
Use a `.env` file to store environment variables (see `.env.example`).

## 🧪 Testing
```bash
pytest
```

## ✅ CI/CD
GitHub Actions runs linting and tests on push.

## 🎥 Demo Video
[Add your video link here]