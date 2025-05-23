from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from textblob import TextBlob # type: ignore

router = APIRouter()

class TextRequest(BaseModel):
    text: str

@router.post("/analyze")
def analyze_sentiment(request: TextRequest):
    blob = TextBlob(request.text)
    polarity = blob.sentiment.polarity
    sentiment = "Neutral"
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    return {"sentiment": sentiment, "polarity": polarity}