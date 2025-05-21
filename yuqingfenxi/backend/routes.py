from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict
from ai_models.ai_service import ModelService

router = APIRouter()
model_service = ModelService()

# 请求模型
class AnalysisRequest(BaseModel):
    text: str
    analysis_type: str  # sentiment|topics|all

# 响应模型
class SentimentResponse(BaseModel):
    sentiment_score: float

class TopicResponse(BaseModel):
    topics: List[Dict[str, Any]]

class FullAnalysisResponse(SentimentResponse, TopicResponse):
    pass

@router.post("/analyze", response_model=FullAnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    """文本分析接口，支持情感分析和主题分析"""
    result = {}
    
    if request.analysis_type in ["sentiment", "all"]:
        result["sentiment_score"] = model_service.analyze_sentiment(request.text)
    
    if request.analysis_type in ["topics", "all"]:
        result["topics"] = model_service.analyze_topics(request.text)
    
    return result