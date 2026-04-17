import pickle
import numpy as np
from flask import Flask, request, render_template

# Initialize app
app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('model/model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

# Prediction route
@app.route('/predict_datapoint', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == "POST":
        try:
          
            income = float(request.form.get('income'))
            loan_amount = float(request.form.get('loan_amount'))
            credit_score = float(request.form.get('credit_score'))
            employment_years = float(request.form.get('employment_years'))
            debt_to_income = float(request.form.get('debt_to_income'))

            data = np.array([[income, loan_amount, credit_score, employment_years, debt_to_income]])

            scaled_data = scaler.transform(data)

            prediction = model.predict(scaled_data)[0]
            probability = model.predict_proba(scaled_data)[0][1]

            if prediction == 1:
                result = f"High Risk ⚠️ (Probability: {probability:.2f})"
            else:
                result = f"Low Risk ✅ (Probability: {probability:.2f})"

            return render_template('index.html', results=result)

        except Exception as e:
            return render_template('index.html', results=f"Error: {str(e)}")

    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)