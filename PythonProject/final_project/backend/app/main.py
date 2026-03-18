from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.db.database import Base, engine
from backend.app.api import auth, user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "ok"}
