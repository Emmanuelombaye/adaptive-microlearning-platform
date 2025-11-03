from fastapi import FastAPI
from backend.app.api.routes import users, courses, quizzes, recommendations

app = FastAPI(
    title="Adaptive Microlearning Platform",
    version="1.0.0",
    description="AI-powered backend for personalized learning"
)

# ? Register routers
app.include_router(users.router)
app.include_router(courses.router)
app.include_router(quizzes.router)
app.include_router(recommendations.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Adaptive Microlearning API!"}
