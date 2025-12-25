import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_next_sales():
    df = pd.read_csv("data/sales.csv")
    df.columns = df.columns.str.strip().str.lower()

    if "date" not in df.columns or "daily_revenue" not in df.columns:
        raise ValueError("CSV must contain 'date' and 'daily_revenue'")

    df["date"] = pd.to_datetime(df["date"])
    df = df.dropna()

    # Aggregate revenue per day
    grouped = df.groupby("date")["daily_revenue"].sum().reset_index()
    grouped["day_index"] = range(1, len(grouped) + 1)

    X = grouped[["day_index"]]
    y = grouped["daily_revenue"]

    if len(X) < 2:
        return float(y.iloc[-1])

    model = LinearRegression()
    model.fit(X, y)

    next_day = [[grouped["day_index"].max() + 1]]
    prediction = model.predict(next_day)

    return round(float(prediction[0]), 2)
