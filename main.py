from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware

app = FastAPI(
  title="Issue Tracker API",
  version="0.1.0",
  description="A mini production-style API built with FastAPI",
)

app.middleware("http")(timer_middleware)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

@app.get("/api/health")
def health_check():
    return { "status": "ok" }

app.include_router(issues_router)
