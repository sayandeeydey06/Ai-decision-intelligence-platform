from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from predictor import predict_next_sales
from decision_engine import make_decision
from actions import perform_action
from fastapi import UploadFile, File
import shutil
from decision_logs import save_decision_log, get_decision_history


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.get("/sales")
def get_sales_data():
    df = pd.read_csv("data/sales.csv")

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    if "date" not in df.columns or "daily_revenue" not in df.columns:
        return {"error": "CSV must contain 'date' and 'daily_revenue'"}

    df = df.dropna()

    # Convert date to datetime
    df["date"] = pd.to_datetime(df["date"])

    # Aggregate revenue per day (important!)
    grouped = df.groupby("date")["daily_revenue"].sum().reset_index()

    # Create numeric day index for chart
    grouped["day_index"] = range(1, len(grouped) + 1)

    return {
        "days": grouped["day_index"].tolist(),
        "sales": grouped["daily_revenue"].tolist(),
        "dates": grouped["date"].dt.strftime("%Y-%m-%d").tolist()
    }


@app.get("/decision")
def decision():
    prediction = predict_next_sales()
    decision_result = make_decision(prediction)
    action_result = perform_action(decision_result)

    log_data = {
        "predicted_sales": prediction,
        "decision": decision_result["decision"],
        "reason": decision_result["reason"],
        "confidence": decision_result["confidence"],
        "action_taken": action_result["action_taken"]
    }

    save_decision_log(log_data)

    return {
        **log_data,
        "timestamp": action_result["timestamp"]
    }

@app.get("/decision-history")
def decision_history():
    return get_decision_history()


@app.get("/predict")
def predict_sales():
    prediction = predict_next_sales()
    return {
        "predicted_next_day_sales": prediction
    }


@app.post("/upload-csv")
def upload_csv(file: UploadFile = File(...)):
    file_location = "data/sales.csv"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "CSV uploaded successfully. AI will now use new data."
    }
