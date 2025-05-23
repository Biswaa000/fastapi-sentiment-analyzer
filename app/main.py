# from fastapi import FastAPI
# from app.api import router as sentiment_router
# from app.config import settings

# app = FastAPI(title=settings.APP_NAME)
# app.include_router(sentiment_router)


# -------------------------------------------------------------------------------

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.api import router as sentiment_router
from app.config import settings
import os

app = FastAPI(title=settings.APP_NAME)

app.include_router(sentiment_router)

# Serve templates and static files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

