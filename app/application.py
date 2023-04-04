import pickle

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # create a FastAPI "instance"

clf = pickle.load(open("model.pkl", "rb"))


class request_body(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float


@app.get("/predict")
def predict(data: request_body):
    test_data = [
        [
            data.age,
            data.sex,
            data.cp,
            data.trestbps,
            data.chol,
            data.fbs,
            data.restecg,
            data.thalach,
            data.exang,
            data.oldpeak,
            data.slope,
            data.ca,
            data.thal,
        ]
    ]

    return {
        "probability of heart disease": round(
            clf.predict_proba([test_data[0]])[0][1], 2
        )
    }
