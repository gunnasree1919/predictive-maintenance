# 🔧 Predictive Maintenance for Manufacturing Equipment

A machine learning-based predictive maintenance system that analyzes sensor data and predicts whether industrial equipment is likely to fail. The application provides an interactive Streamlit dashboard for real-time failure prediction.

---

##  Project Overview

Predictive Maintenance helps industries reduce downtime, maintenance costs, and unexpected equipment failures by using machine learning to identify potential faults before they occur.

This project uses sensor measurements such as:

- Temperature (TP1_iiot)
- Pressure (PE1_iiot)
- Vibration/Flow (FM1_iiot)

to predict whether a machine is operating normally or is likely to fail.

---

## Features

Machine Failure Prediction

Interactive Streamlit Dashboard

Real-Time Sensor Input Analysis

Pre-trained Machine Learning Model

User-Friendly Interface

Instant Prediction Results

---

## 🛠️ Technologies Used

- Python
- Streamlit
- NumPy
- Scikit-Learn
- Joblib
- Machine Learning

---

##  Project Structure

```text
Predictive-Maintenance/
│
├── app.py
├── predictive_model.pkl
├── Maintanence_dataset.csv
├── predictive maintenance.ipynb
├── README.md
└── screenshots/
```

---

## Dataset

The model is trained using industrial sensor data containing machine operational parameters such as:

- Temperature
- Pressure
- Vibration
- Flow Measurements

These features are standardized and used for machine failure prediction.

---

##  Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Predictive-Maintenance.git
cd Predictive-Maintenance
```

### Install Dependencies

```bash
pip install streamlit numpy scikit-learn joblib
```

---

##  Run Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## Application Screenshots

### Home Dashboard

![Dashboard](screenshots/dashboard.png)

### Sensor Input Interface

![Input Screen](screenshots/input.png)

### Normal Machine Prediction

![Normal Prediction](screenshots/normal_prediction.png)

### Failure Prediction Alert

![Failure Alert](screenshots/failure_alert.png)

---

##  Workflow

1. User enters sensor values.
2. Sensor data is processed.
3. Trained ML model analyzes inputs.
4. Prediction is generated.
5. Dashboard displays:

   - Normal Operation 
   - Failure Alert 

---

##  Prediction Output

### Normal Condition

```text
Machine is functioning normally.
```

### Failure Condition

```text
ALERT: Machine is likely to FAIL soon!
```

---

##  Future Enhancements

- Real-time IoT sensor integration
- Cloud deployment
- Predictive analytics dashboard
- Maintenance scheduling system
- SMS/Email alerts
- Equipment health monitoring

---

## Author

**Y. Gunna Sree**

B.Tech – Artificial Intelligence & Machine Learning

SRM University AP

---

## 📄 License

This project is developed for educational and research purposes.
