from fastapi import FastAPI
import random

app = FastAPI(title="NeuraLearn ML Service", version="1.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML microservice"}

@app.get("/predict_skill_gap")
def predict_skill_gap(user_id: int):
    # Dummy logic for now
    skill_score = random.uniform(0, 1)
    gap = "High" if skill_score < 0.3 else "Medium" if skill_score < 0.7 else "Low"
    return {"user_id": user_id, "predicted_gap": gap, "confidence": round(skill_score, 2)}
