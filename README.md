# Heart Stroke Prediction - My First Machine Learning Project

This project was my first end-to-end machine learning project completed during my diploma. It focuses on predicting whether a patient is at risk of stroke based on their medical and personal information.

---

## 🎯 Project Objective

- Predict whether a person will experience a stroke based on health indicators.
- Understand and practice an end-to-end machine learning workflow: 
  - Data preprocessing
  - Model training
  - Model evaluation
  - (Attempted) Deployment Integration using Flask

---

## 📊 Dataset Description

The dataset includes features such as:

- Age
- Gender
- Hypertension
- Heart Disease
- Marital Status
- Work Type
- Residence Type
- Average Glucose Level
- BMI
- Smoking Status
- Stroke (Target variable)

---

## ⚙️ Project Workflow

### 1️⃣ Data Preprocessing
- Handled missing values.
- Encoded categorical features using Label Encoding & One-Hot Encoding.
- Scaled numerical features using StandardScaler.
- Split data into train and test sets.

### 2️⃣ Model Building
- Built classification models using algorithms like:
  - Logistic Regression
  - Random Forest
  - Support Vector Machines
- Evaluated using metrics like accuracy, precision, recall, F1-score, and confusion matrix.

### 3️⃣ Deployment Attempt (First Learning Experience)
- Tried to integrate the model into a Flask web app for live prediction.
- Faced challenges:
  - The preprocessing done during training could not be directly applied to new test data.
  - The pipeline failed because the new input data was not transformed the same way as training data.
  - Learned that order and structure of input features must exactly match the model's expectation during inference.

---

## 📌 Key Learning from This Project

✅ **Importance of Preprocessing Pipelines:**  
- Learned to build preprocessing as a separate object (using `Pipeline`, `ColumnTransformer` etc.)  
- Understood how to save both preprocessing objects and models for future use.

✅ **Model-Input Alignment:**  
- The order of input features during prediction must exactly match the order during model training.

✅ **Deployment Challenges:**  
- Deployment isn't just about training models; it's about ensuring consistent data processing from start to end.
- Learned how to package preprocessing + model together for smooth integration into Flask later in my journey.

✅ **Error Handling & Debugging:**  
- Gained valuable debugging experience in managing ML serving pipelines.

---

## 🖥 Technologies Used

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib / Seaborn
- Jupyter Notebook
- Flask (Deployment Attempt)

---

## 🚀 How I Would Improve This Project Today

- Build a complete ML pipeline using `Pipeline()` or `ColumnTransformer()`.
- Serialize both preprocessing and model using `joblib` or `pickle`.
- Create a fully functional Flask app that takes user input, applies preprocessing, and makes predictions.
- Write validation functions to check for correct input formats before prediction.

---

## 📖 Author

- **Your Name**
- GitHub: [vijay](https://github.com/vijay33391)

---

## ⚠️ Disclaimer

> This project was my first machine learning project. While not perfect, it gave me valuable hands-on experience and exposed me to real-world challenges that ML engineers often face.

