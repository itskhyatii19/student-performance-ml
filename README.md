# 🎓 Student Performance Prediction – End-to-End ML Project

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)
![Status](https://img.shields.io/badge/Status-Portfolio%20Project-success)
![License](https://img.shields.io/badge/License-MIT-green)
![Dataset](https://img.shields.io/badge/Dataset-Kaggle-lightgrey)

> An **end-to-end machine learning pipeline** to predict students’ final grades using real-world educational data.  
Built as a **portfolio project** to demonstrate practical ML workflows, clean project structuring, and evaluation.

---

## 📌 Project Overview

This project predicts the **final grade (G3)** of students based on academic performance, family background, and lifestyle factors.

The **Actual vs Predicted** plot shows strong alignment along the diagonal, indicating:
- Low prediction error
- Good generalization performance

---

## 🗂 Project Structure

student-performance-ml/
│
├── data/
│ ├── raw/
│ │ └── student_data.csv
│ ├── processed/
│ │ ├── cleaned_data.csv
│ │ └── features.csv
│
├── src/
│ ├── data_cleaning.py
│ ├── eda.py
│ ├── feature_engineering.py
│ ├── train_model.py
│ ├── evaluation.py
│ └── predict.py
│
├── model.pkl
├── requirements.txt
└── README.md


---

## 📊 Dataset

- **Source:** Kaggle – Student Performance Dataset  
- **Rows:** ~395  
- **Features:** Academic, family, and lifestyle factors  
- **Target Variable:** Final Grade (`G3`)

---

## 🔁 Machine Learning Pipeline

### 1️⃣ Data Cleaning
- Remove duplicate rows  
- Handle missing numeric values  
- Save cleaned dataset  

### 2️⃣ Exploratory Data Analysis (EDA)
- Grade distribution analysis  
- Correlation heatmaps  
- Feature trend analysis  

### 3️⃣ Feature Engineering
- One-hot encoding for categorical variables  
- Feature selection  
- Save engineered feature set  

### 4️⃣ Model Training
- Train / Test split  
- **Ridge Regression**  
- Model persistence using `joblib`  

### 5️⃣ Evaluation
- Mean Absolute Error (MAE)  
- R² Score  
- Actual vs Predicted visualization  

---

## 📈 Model Performance

| Metric | Value |
|------|------|
| **MAE** | ~0.95 |
| **R² Score** | ~0.83 |

✔ Indicates strong predictive performance  
✔ Low average prediction error  

---

## 🔍 Key Insights

- **Previous exam score (G2)** is the strongest predictor  
- **Family support** positively impacts performance  
- **Parental profession** shows measurable influence  
- Students from **urban areas** perform slightly better  
- Feature importance extracted from **Ridge Regression coefficients**

---

## ▶ How to Run

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Data cleaning
python src/data_cleaning.py
3️⃣ Feature engineering
python src/feature_engineering.py
4️⃣ Train model
python src/train_model.py
5️⃣ Evaluate model
python src/evaluation.py
6️⃣ Make prediction
python src/predict.py --g2 15 --failures 0 --famsup yes --medu 4
🛠 Tech Stack
Python

Pandas

NumPy

Matplotlib

Scikit-learn

🚀 Future Improvements
Experiment with tree-based models

Hyperparameter tuning

Cross-validation

Deploy as a web application

👩‍💻 Author
Khyati Sharma
🎓 B.Tech AI Student
💻 Aspiring Machine Learning Engineer

📌 About
End-to-end machine learning pipeline to predict student performance using real-world data. Includes data cleaning, feature engineering, model training, evaluation, and interpretation.

⭐ Support
If you found this project useful, consider giving it a ⭐
It helps me stay motivated to build more!

