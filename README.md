# 💳 Credit Risk Prediction System

A Machine Learning-powered web application that predicts whether a person is likely to default on a loan based on financial and behavioral attributes.

---

## 🚀 Project Overview

This project uses **Logistic Regression** with hyperparameter tuning to classify loan applicants into:

* ✅ **Low Risk**
* ⚠️ **High Risk**

The model is deployed using **Flask**, allowing users to input data and get real-time predictions.

---

## 🧠 Features

* Predicts loan default risk using ML
* Real-time predictions via web interface
* Scaled input using StandardScaler
* Hyperparameter tuning using GridSearchCV
* Model evaluation using ROC-AUC, Confusion Matrix, Accuracy
* Model is deployed in AWS ElasticBeanStalk and using codepipeline ti import model from Github

---

## 📊 Input Features

| Feature              | Description                    |
| -------------------- | ------------------------------ |
| Income               | Annual income of the applicant |
| Loan Amount          | Amount of loan requested       |
| Credit Score         | Financial reliability score    |
| Employment Years     | Years of job experience        |
| Debt-to-Income Ratio | Financial burden indicator     |

---

## ⚙️ Tech Stack

* Python
* Scikit-learn
* Flask
* NumPy
* HTML/CSS
* AWS ElasticBeanStalk

---

## 🏗️ Project Structure
credit-risk-model/
│
├── application.py
├── requirements.txt
├── Procfile
├── model/
│ ├── model.pkl
│ └── scaler.pkl
├── templates/
│ └── index.html
├── README.md


---

## 🧪 Model Details

* Model: Logistic Regression
* Hyperparameter Tuning: GridSearchCV
* Evaluation Metrics:
  * Accuracy
  * ROC-AUC Score
  * Confusion Matrix
* Deployment on AWS
---

## ▶️ How to Run Locally

1. Clone the repository
git clone https://github.com/mayank-1584/credit_risk_model.git

cd credit-risk-model


2. Install dependencies

pip install -r requirements.txt


3. Run the Flask app

python application.py


4. Open in browser

http://localhost:5000


---

## 📈 Sample Output

* Low Risk ✅ (0.23 probability)
* High Risk ⚠️ (0.78 probability)

---

## 🎯 AWS detail

* Deploy on AWS ElasticBeanStalk
* But due to cost issue the project is not live

---

## 👨‍💻 Author

Mayank Sharma  
Aspiring Software Engineer  

---
