import React, { useEffect, useState } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";

// 🔗 LIVE BACKEND URL (Render)
const API_BASE = "https://ai-decision-backend.onrender.com";

function App() {
  const [salesData, setSalesData] = useState([]);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  // Fetch all backend data
  const loadData = () => {
    setLoading(true);

    // Sales data
    fetch(`${API_BASE}/sales`)
      .then(res => res.json())
      .then(data => {
        if (data.days && data.sales) {
          const formatted = data.days.map((day, i) => ({
            day,
            sales: data.sales[i]
          }));
          setSalesData(formatted);
        }
      })
      .catch(err => console.error("Sales error:", err));

    // Decision + action (also creates history entry)
    fetch(`${API_BASE}/decision`)
      .then(res => res.json())
      .then(data => {
        setResult(data);
        setLoading(false);
      })
      .catch(err => {
        console.error("Decision error:", err);
        setLoading(false);
      });

    // Decision history
    fetch(`${API_BASE}/decision-history`)
      .then(res => res.json())
      .then(data => setHistory(data))
      .catch(err => console.error("History error:", err));
  };

  useEffect(() => {
    loadData();
  }, []);

  // CSV Upload Handler
  const handleUpload = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    fetch(`${API_BASE}/upload-csv`, {
      method: "POST",
      body: formData
    })
      .then(res => res.json())
      .then(data => {
        alert(data.message);
        loadData(); // reload everything with new CSV
      })
      .catch(() => alert("CSV upload failed"));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Autonomous AI Decision Intelligence Platform</h1>

      {/* CSV Upload */}
      <h3>📁 Upload Sales CSV</h3>
      <input type="file" accept=".csv" onChange={handleUpload} />

      <hr />

      {/* Chart */}
      <h3>📊 Sales Analytics</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={salesData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="day" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="sales" strokeWidth={3} />
        </LineChart>
      </ResponsiveContainer>

      {/* Decision */}
      {loading && <p>⏳ Updating AI...</p>}

      {result && !loading && (
        <>
          <h3>🧠 AI Decision</h3>
          <p><b>Prediction:</b> {result.predicted_sales}</p>
          <p><b>Decision:</b> {result.decision}</p>
          <p><b>Reason:</b> {result.reason}</p>
          <p><b>Confidence:</b> {result.confidence}</p>

          <h3>⚡ Autonomous Action</h3>
          <p>{result.action_taken}</p>
          <small>{result.timestamp}</small>
        </>
      )}

      <hr />

      {/* Decision History */}
      <h3>📜 Decision History</h3>

      {history.length === 0 ? (
        <p>No decisions logged yet.</p>
      ) : (
        <table border="1" cellPadding="6">
          <thead>
            <tr>
              <th>Time</th>
              <th>Prediction</th>
              <th>Decision</th>
              <th>Confidence</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {history.slice().reverse().map((item, index) => (
              <tr key={index}>
                <td>{item.timestamp}</td>
                <td>{item.predicted_sales}</td>
                <td>{item.decision}</td>
                <td>{item.confidence}</td>
                <td>{item.action_taken}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default App;
