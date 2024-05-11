from fastapi import FastAPI
from .models import user as user_model
from .core.database import engine
from .routes import auth

user_model.Base.metadata.create_all(bind=engine)

summary = """
API для KATIS. 🚀
"""

app = FastAPI(
title="Katis",
    summary=summary,
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Рахимян Тимерханов",
        # "url": "http://x-force.example.com/contact/",
        "email": "timerkhanov.ri@phystech.edu",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Welcome to my API"}

