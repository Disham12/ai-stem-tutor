from fastapi import FastAPI
from ai_stem_tutor.routers import ask, solve, retrieve, explain
# from ai_stem_tutor.routers import speech


app = FastAPI(title="AI STEM Tutor")

app.include_router(ask.router)
app.include_router(solve.router)
app.include_router(retrieve.router)
app.include_router(explain.router)
# app.include_router(speech.router)
@app.get("/")
def read_root():
    return {"message": "AI STEM Tutor backend is running."}
