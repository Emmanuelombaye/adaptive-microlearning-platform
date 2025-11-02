from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_recommendations():
    return {"recommendations": ["Review Python OOP", "Take ML Refresher"]}
