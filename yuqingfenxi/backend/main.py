# 项目初始化代码
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict, Any
import uvicorn

app = FastAPI(
    title="舆情分析系统API",
    description="基于BERT的舆情分析服务",
    version="1.0.0"
)

# 基础数据模型
class RawDataRequest(BaseModel):
    content: str
    source: str

class AnalysisResult(BaseModel):
    sentiment: float
    topics: List[str]
    priority: int

# 注册API路由
from routes import router as analysis_router
app.include_router(analysis_router, prefix="/api")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)