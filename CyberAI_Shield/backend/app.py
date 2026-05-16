from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # Lướt dòng này vào
from pydantic import BaseModel
import pickle
import os

app = FastAPI(title="CyberAI Shield API", description="API phân tích lỗi hệ thống bằng AI")

# --- CẤU HÌNH CORS ĐỂ FRONTEND CÓ THỂ GỌI API ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Trong phát triển cho phép tất cả, khi lên SaaS thương mại sẽ điền domain của web vào đây
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_PATH = "../models/bsod_model.pkl"
if os.path.exists(MODEL_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
else:
    model = None

class LogRequest(BaseModel):
    Bugcheck_String: str
    Faulting_Module: str
    Crash_Code: str

@app.get("/")
def health_check():
    return {"status": "success", "message": "CyberAI Shield API đang hoạt động!"}

@app.post("/api/analyze")
def analyze_log(request: LogRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Hệ thống AI chưa sẵn sàng.")
    
    combined_text = f"{request.Bugcheck_String} {request.Faulting_Module} {request.Crash_Code}"
    prediction = model.predict([combined_text])
    
    return {
        "analyzed_data": request.model_dump(),
        "root_cause_prediction": prediction[0]
    }