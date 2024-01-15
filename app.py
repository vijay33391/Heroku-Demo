#Certainly! Below is the modified `app.py` code that uses a RandomForest model (loaded from a pickled file named 'random_forest_model_pkl.pkl') to predict the outcome based on the form inputs:

from flask import Flask, render_template, request
import pickle
import numpy as n


app = Flask(__name__)
model = pickle.load(open('with_out_random_forest_model.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extracting form input values
        gender = request.form['gender']
        age = int(request.form['age'])
        hypertension = int(request.form['hypertension'])
        heart_disease = int(request.form['heart_disease'])
        ever_married = request.form['ever_married']
        work_type = request.form['work_type']
        residence_type = request.form['residence_type']
        avg_glucose_level = float(request.form['avg_glucose_level'])
        bmi = float(request.form['bmi'])
        smoking_status = request.form['smoking_status']

        # Convert categorical features to numerical values
        gender = 1 if gender == 'Male' else 0
        ever_married = 1 if ever_married == 'Yes' else 0
        residence_type = 1 if residence_type == 'Urban' else 0
        work_type_encoded = {
            'children': 0,
            'Govt_jov': 1,
            'Never_worked': 2,
            'Private': 3,
            'Self-employed': 4
        }
        smoking_status_encoded = {
            'formerly_smoked': 0,
            'never_smoked': 1,
            'smokes': 2,
            'Unknown': 3
        }
        work_type = work_type_encoded.get(work_type, 0)
        smoking_status = smoking_status_encoded.get(smoking_status, 0)

        # Making prediction using the loaded model
        prediction = model.predict([[gender, age, hypertension, heart_disease, ever_married, work_type, residence_type, avg_glucose_level, bmi, smoking_status]])
        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'The predicted outcome is: {output}')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


