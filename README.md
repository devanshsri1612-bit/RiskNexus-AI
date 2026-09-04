# 🛡️ RiskNexus AI

> AI-Powered Financial Risk Intelligence Platform for Fraud Detection, Merchant Trust Analysis, and Transaction Investigation.

## 📌 Overview

RiskNexus AI is an intelligent transaction risk assessment system designed to identify potentially fraudulent financial activities using multiple layers of analysis.

The platform combines:

- Behavioral Risk Analysis
- Merchant Trust Scoring
- Graph-Based Relationship Investigation
- Intelligent Decision Engine
- Explainable AI Summaries

to generate actionable decisions such as:

✅ ALLOW  
⚠️ REVIEW  
🚫 BLOCK

---

## 🚀 Key Features

### 🧠 Behavioral DNA Engine
Analyzes transaction behavior patterns and detects anomalies based on:

- Transaction amount
- Device changes
- Location mismatch
- User behavior deviations

---

### ⚠️ Risk Engine

Converts behavioral anomalies into a quantitative risk score.

Outputs:

- Risk Score (0–100)
- Risk Level
- Fraud Indicators

---

### 🏪 TrustLens Engine

Evaluates merchant credibility using:

- Merchant ratings
- Customer complaints
- Chargebacks

Outputs:

- Trust Score
- Trust Classification

(TRUSTED / MODERATE / RISKY)

---

### 🕸️ Graph Investigation Engine

Identifies suspicious connections between:

- Users
- Devices
- Merchants

Detects hidden risk networks and relationship patterns.

Outputs:

- Connected Entities
- Graph Risk Level

---

### 🤖 Intelligent Decision Engine

Combines outputs from:

- Risk Engine
- TrustLens
- Graph Engine

to generate:

- Final Decision
- Confidence Score
- Investigation Summary

---

### 📊 Interactive Dashboard

Built using Streamlit.

Features:

- Transaction Analysis Interface
- Risk Visualization
- Trust Comparison Charts
- AI Investigation Summary
- Downloadable Investigation Reports

---

## 🏗️ System Architecture

```text
Transaction
      │
      ▼
Behavioral DNA Engine
      │
      ▼
Risk Engine
      │
 ┌────┴────┐
 ▼         ▼
TrustLens  Graph Engine
      │
      ▼
Decision Engine
      │
      ▼
ALLOW / REVIEW / BLOCK
```

---

## 📸 Dashboard Screenshots

### Home Dashboard

Add screenshot here

### Transaction Analysis

Add screenshot here

### AI Investigation Summary

Add screenshot here

### Risk Visualization

Add screenshot here

---

## 🛠️ Technology Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| Dashboard | Streamlit |
| Data Processing | Pandas |
| Storage | CSV Files |
| Analytics | Custom Rule Engine |
| Visualization | Streamlit Charts |

---

## 📂 Project Structure

```text
RiskNexus-AI/
│
├── app.py
├── behavioral_dna.py
├── risk_engine.py
├── trustlens.py
├── graph_engine.py
├── decision_engine.py
│
├── transactions.csv
├── merchant.csv
├── users.csv
├── graph_data.csv
│
├── architecture.png
├── README.md
│
└── screenshots/
```

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/devanshsri1612-bit/RiskNexus-AI.git
```

### Navigate to Project

```bash
cd RiskNexus-AI
```

### Install Dependencies

```bash
pip install streamlit pandas
```

### Launch Dashboard

```bash
streamlit run app.py
```

---

## 📈 Sample Output

```json
{
  "Transaction": "TX011",
  "User": "U004",
  "Merchant": "M002",
  "Risk Score": 100,
  "Trust Score": 13,
  "Graph Risk": "HIGH",
  "Decision": "BLOCK",
  "Confidence": "95%"
}
```

---

## 🎯 Business Impact

RiskNexus AI helps financial institutions:

- Reduce fraud losses
- Detect suspicious merchant activity
- Improve investigation efficiency
- Enable explainable decision-making
- Strengthen transaction monitoring systems

---

## 🔮 Future Enhancements

- Real-Time Transaction Streaming
- Graph Neural Networks (GNNs)
- Machine Learning Risk Models
- Merchant Reputation APIs
- Explainable AI Reports
- Real-Time Alerting System

---
## 📸 Screenshots

### Dashboard
![Dashboard](Screenshot%202026-09-04%20201201.png)

### Transaction Analysis
![Analysis](Screenshot%202026-09-04%20201457.png)

### AI Investigation Summary
![AI Summary](Screenshot%202026-09-04%20201526.png)

### Risk vs Trust Analysis
![Graph](Screenshot%202026-09-04%20201254.png)

### Investigation Report
![Report](Screenshot%202026-09-04%20201228.png)

## 👨‍💻 Developed By

**Devansh Srivastava**

Built as a Financial Risk Intelligence & Fraud Detection Project using Python and Streamlit.
