from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_courses():
    return {"courses": ["Python Basics", "ML Fundamentals", "React Essentials"]}
