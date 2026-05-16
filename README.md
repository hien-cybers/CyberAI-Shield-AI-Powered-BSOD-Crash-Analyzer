# 🛡️ CyberAI Shield: AI-Powered BSOD Crash & Vulnerability Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18.x-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-8.x-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)

**CyberAI Shield** is an advanced full-stack Machine Learning application engineered to assist Blue Teams and Security Operations Center (SOC) Analysts. It automates the extraction, processing, and analysis of Windows system crash logs (BSOD Logs) to detect early indicators of critical vulnerability exploitations in real-time.

This project showcases a complete end-to-end software and data engineering pipeline: parsing unstructured system text logs, training and packaging a machine learning model, exposing the model via a high-performance RESTful API, and displaying results on a responsive front-end cybersecurity dashboard.

---

## 🏗️ Core Architecture & Data Flow

The application utilizes a decoupled Client-Server architecture with a dedicated Machine Learning pipeline:

```text
[User Input] ──> [React Frontend (Port 5173)] 
                        │  (JSON Payload via HTTP POST)
                        ▼
           [FastAPI Backend (Port 8000)]
                        │  (Vectorization via TF-IDF)
                        ▼
         [Random Forest Classifier (.pkl)] ──> [Vulnerability/Root Cause Prediction]
```

1. **Log Parsing Engine:** Utilizes optimized Regular Expressions (Regex) to extract technical signatures (`Bugcheck_String`, `Faulting_Module`, `Crash_Code`) from raw text dumps.
2. **AI Inference Pipeline:** Transforms categorical text features into mathematical matrices using a **TF-IDF Vectorizer**, which are then classified by a trained **Random Forest Model** to map system symptoms to specific known CVEs.
3. **Reactive Communication:** Features full-duplex asynchronous data fetching paired with secure Cross-Origin Resource Sharing (CORS) policies.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend UI** | ReactJS, Vite, JavaScript (ES6+), Modern Dark-Theme CSS |
| **Backend API** | Python, FastAPI, Uvicorn ASGI Server, CORS Middleware |
| **Machine Learning** | Scikit-learn (Random Forest), Pandas, NumPy, Pickle |
| **Data Processing** | Regular Expressions (Regex), Structured CSV pipelines |

---

## 📂 Project Directory Structure

```text
CyberAI_Shield/
├── backend/
│   ├── app.py                 # FastAPI Server initialization & CORS configuration
│   ├── create_dataset.py      # Automated script to generate training dataset (.csv)
│   ├── log_parser.py          # Advanced Regex-based log extraction logic
│   ├── test_model.py          # Local model performance evaluation suite
│   └── train_model.py         # ML model training, evaluation, and serialization script
├── data/
│   ├── bsod_dataset.csv       # Structured and labeled historical crash dataset
│   └── sample_bsod.txt        # Raw unstructured system crash log dump example
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Core React Dashboard component & API integration
│   │   └── main.jsx           # Frontend DOM rendering entrypoint
│   ├── package.json           # Frontend Node dependencies & scripts
│   └── vite.config.js         # Vite bundler configurations
├── models/
│   └── bsod_model.pkl         # Serialized high-accuracy Random Forest model artifact
└── .gitignore                 # Strict rules excluding venv/ and node_modules/ from version control
```

---

## 🚀 Installation & Local Deployment Guide

To deploy this infrastructure locally, launch **two separate terminal split-panes** in your IDE to run the services concurrently.

### Prerequisites
* Python 3.10 or higher installed
* Node.js v18+ and npm installed

### Step 1: Initialize the Backend Server (FastAPI)

1. Open your first terminal window, navigate to the root directory, and activate your isolated virtual environment:
   ```powershell
   .\venv\Scripts\activate
   ```
2. Change directory into the backend microservice:
   ```powershell
   cd CyberAI_Shield\backend
   ```
3. Run the hot-reloading production web server:
   ```powershell
   uvicorn app:app --reload
   ```
   *The local API gateway will securely listen at:* `http://127.0.0.1:8000`

### Step 2: Initialize the Frontend Client (React + Vite)

1. Open your second terminal window (click the `+` icon in the VS Code terminal bar).
2. Change directory directly into the frontend user interface app:
   ```powershell
   cd CyberAI_Shield\frontend
   ```
3. Launch the reactive frontend server explicitly bound to the global IPv4 host:
   ```powershell
   npm run dev -- --host
   ```
   *The interactive system security dashboard will be accessible at:* `http://127.0.0.1:5173/`

---

## 🛡️ Real-World Exploit Verification Scenario

To test the security intelligence and accuracy of the underlying machine learning model:

1. Launch the frontend dashboard in your browser via `http://127.0.0.1:5173/`.
2. Input the following technical crash payload harvested from an active exploitation scenario:
   * **Bugcheck String:** `0xC0000005`
   * **Faulting Module:** `http.sys`
   * **Crash Code:** `ACCESS_VIOLATION`
3. Click the **Gửi Yêu Cầu Phân Tích** (Submit Analysis) button.
4. **AI Inference Result:** The machine learning brain immediately recognizes the specific kernel heap allocation mismatch signature and flags the root cause: **`Lỗ hổng Bảo mật (Gợi ý: CVE-2022-21907)`** (A well-known Windows Remote Code Execution vulnerability).

---

## 👥 Author & Maintainer

* **Duc Hien (hien-cybers)**
  * *Role:* Full-Stack Software & AI Security Engineer
  * *GitHub:* [@hien-cybers](https://github.com/hien-cybers)
  * *Academic Focus:* Information Technology & Software Engineering (Specializing in Intelligent Cybersecurity Utilities)

---

## 📝 Roadmap & Future Extensions

This repository serves as an academic foundation for embedding AI architectures into active defensive security pipelines. Future iterations will focus on:
* Integrating real-time Windows native binary kernel dump parsing directly from `.dmp` files.
* Expanding the core multi-class dataset to cover 50+ enterprise-grade OS panic behaviors.
