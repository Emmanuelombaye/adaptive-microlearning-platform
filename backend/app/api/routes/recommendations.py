from fastapi import APIRouter

router = APIRouter(
    prefix="/api/recommendations",
    tags=["Recommendations"]
)

@router.get("/")
def get_recommendations():
    return {"recommendations": ["Focus on AI basics", "Try the next micro-lesson on Python"]}
