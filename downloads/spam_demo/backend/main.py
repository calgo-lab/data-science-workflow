from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

app = FastAPI(title="Spam Demo API", version="0.1.0")


def random_email() -> dict[str, str]:
    return {
        "subject": str(np.random.choice(["Urgent invoice update", "Meeting reminder", "Free gift card inside", "Account verification needed"])),
        "body": str(np.random.choice(["Please review the attached note.", "Click now to claim your prize.", "Open attachment for details.", "See details at your convenience."]))
    }


def model_predict(email: dict[str, str], spam_probability: float) -> str:
    np.random.seed(hash(email.__str__()) % (2**8))
    return np.random.choice(["Spam", "Not spam"], p=[spam_probability, 1 - spam_probability])


class PredictRequest(BaseModel):
    subject: str
    body: str
    spam_probability: float


@app.get("/sample")
def sample() -> dict[str, str]:
    return random_email()


@app.post("/predict")
def predict(request: PredictRequest) -> dict[str, str]:
    email = {"subject": request.subject, "body": request.body}
    prediction = model_predict(email, request.spam_probability)
    return {"prediction": prediction}
