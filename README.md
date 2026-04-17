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

* **Python**
* **Scikit-learn**
* **Flask**
* **NumPy**
* **HTML/CSS**

---

## 🏗️ Project Structure

```
credit-risk-model/
│
├── application.py
├── model/
│   ├── model.pkl
│   └── scaler.pkl
├── templates/
│   └── index.html
├── README.md
```

---

## 🧪 Model Details

* Model: Logistic Regression
* Hyperparameter Tuning: GridSearchCV
* Evaluation Metrics:

  * Accuracy
  * ROC-AUC Score
  * Confusion Matrix

---

## ▶️ How to Run Locally

1. Clone the repository

```
git clone <your-repo-link>
cd credit-risk-model
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the Flask app

```
python application.py
```

4. Open in browser

```
http://localhost:5000
```

---

## 📈 Sample Output

* **Low Risk ✅ (0.23 probability)**
* **High Risk ⚠️ (0.78 probability)**

---

## 🎯 Future Improvements

* Deploy on AWS / Render / Railway
* Add authentication system
* Improve UI with modern frontend frameworks
* Use advanced models (XGBoost, Random Forest)

---

## 👨‍💻 Author

**Mayank Sharma**
Aspiring Software Engineer & Quant Enthusiast

---

## ⭐ If you found this useful

Give it a star ⭐ and share it!
