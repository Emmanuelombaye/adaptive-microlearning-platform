from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_quizzes():
    return {"quizzes": ["Intro Quiz", "ML Test", "React Challenge"]}
