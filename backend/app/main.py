from fastapi import FastAPI
from app.api.routes import users, courses, quizzes, recommendations

app = FastAPI(title="NeuraLearn API", version="1.0")

# Include Routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(quizzes.router, prefix="/quizzes", tags=["Quizzes"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])

@app.get("/")
def root():
    return {"message": "Welcome to NeuraLearn Adaptive Micro-Learning API"}
