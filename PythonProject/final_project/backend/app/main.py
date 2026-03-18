from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response, RedirectResponse
from fastapi.staticfiles import StaticFiles
from backend.app.db.database import Base, engine
from backend.app.api import auth, user

app = FastAPI()

FRONTEND_DIR = Path(__file__).resolve().parents[2] / "fontend"

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:8000",
        "http://localhost:8000",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)

app.mount("/assets", StaticFiles(directory=FRONTEND_DIR), name="assets")

@app.get("/")
def root():
    return FileResponse(FRONTEND_DIR / "frontend.html")


@app.get("/frontend")
def frontend():
    return RedirectResponse(url="/", status_code=307)


@app.get("/fontend")
def fontend():
    return RedirectResponse(url="/", status_code=307)


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return Response(status_code=204)
