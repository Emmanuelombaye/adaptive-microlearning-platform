from fastapi import APIRouter
from main.utils.logger import logger

router = APIRouter(prefix="/api/quizzes", tags=["Quizzes"])

@router.get("/")
def get_quizzes():
    logger.info("Fetched quizzes")
    return {"quizzes": ["Quiz 1", "Quiz 2"]}
