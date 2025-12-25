# Autonomous AI Decision Intelligence Platform

An end-to-end **AI-powered decision intelligence system** that analyzes retail sales data, predicts future revenue, generates **explainable business decisions**, and executes **autonomous actions** through a full-stack web application.

---

## 📌 Overview

This project demonstrates how AI can be used **beyond predictions** to support real business decision-making.

Instead of focusing only on model accuracy, the platform emphasizes:
- Decision intelligence
- Explainability
- Automation
- Real-world data handling

The system simulates how AI is applied in **retail analytics and operations**.

---

## 🚀 Features

### 🔹 Data Ingestion
- Supports real-world retail CSV data
- Default dataset included for demo
- Users can upload their own CSV files
- Automatic data aggregation and validation

### 🔹 Machine Learning Prediction
- Predicts next-day revenue using historical trends
- Uses **Linear Regression** for interpretability
- Model retrains automatically when new data is uploaded

### 🔹 Decision Intelligence Engine
- Converts predictions into business decisions
- Generates:
  - Decision
  - Reason
  - Confidence level
- Example decisions:
  - Increase inventory
  - Maintain inventory
  - Reduce inventory

### 🔹 Autonomous Actions
- Executes actions automatically based on decisions
- Example: inventory alert generation
- No manual intervention required

### 🔹 Explainable AI (Decision History)
- Stores decision logs with timestamps
- Maintains a complete audit trail:
  - Prediction
  - Decision
  - Confidence
  - Action taken

### 🔹 Frontend Dashboard
- Interactive sales analytics chart
- AI prediction and decision display
- Autonomous action output
- Decision history table

---

## 🏗️ Architecture

CSV Data (Default / User Upload)
↓
Data Processing & Aggregation
↓
ML Prediction Engine
↓
Decision Engine (Rules + Confidence)
↓
Autonomous Action Executor
↓
Decision History (Audit Logs)
↓
React Dashboard



---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- Pandas
- Scikit-learn

### Frontend
- React
- Recharts
- REST APIs

### Data
- CSV-based ingestion
- Real retail transaction dataset

---

## 📂 Project Structure

AI-Decision-Intelligence-Platform/
│
├── backend/
│ ├── main.py
│ ├── predictor.py
│ ├── decision_engine.py
│ ├── actions.py
│ ├── decision_logs.py
│ ├── data/
│ │ ├── sales.csv
│ │ └── decision_history.json
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ ├── public/
│ └── package.json
│
├── .gitignore
└── README.md


---

## ▶️ How to Run Locally

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
uvicorn main:app --reload


Backend runs at:

http://127.0.0.1:8000

Frontend Setup
cd frontend
npm install
npm start


Frontend runs at:

http://localhost:3000

CSV Requirements

Minimum required columns:

date,daily_revenue


Example:
date,daily_revenue
2024-11-01,13500
2024-11-02,14200
2024-11-03,12800

Sample Output

Prediction:
Predicted Revenue: 11113.87


Decision:
Increase inventory
Reason: High demand expected
Confidence: High