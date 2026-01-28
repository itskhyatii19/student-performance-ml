# 🎓 Student Performance Prediction – End-to-End Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-brightgreen.svg)
![Status](https://img.shields.io/badge/Project-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

---

## 📌 Overview

This project implements a **complete end-to-end machine learning pipeline** to predict student academic performance using real-world educational data.  
It demonstrates practical skills in **data preprocessing, exploratory data analysis (EDA), feature engineering, model training, evaluation, and prediction**.

The project is designed to reflect **industry-style ML workflows**, with modular scripts and a clean project structure.

---

## 🎯 Problem Statement

Educational institutions often struggle to identify students who may be at academic risk early enough to provide targeted support.

The objective of this project is to build a predictive model that estimates student performance based on academic, demographic, and behavioral features, helping uncover key factors influencing academic outcomes.

---

## 📊 Dataset

- **Source:** Student Performance Dataset (UCI / Kaggle)
- **Raw Data:** `data/raw/student_data.csv`
- **Processed Data:**  
  - `data/processed/cleaned_data.csv`  
  - `data/processed/features.csv`
- **Target Variable:** Student performance score / grade
- **Features Include:**
  - Demographic information
  - Study-related habits
  - Academic history

---

## 🧠 Machine Learning Pipeline

The project follows a structured ML workflow:

1. **Data Cleaning**
   - Handling missing values
   - Removing inconsistencies
   - Cleaning raw input data

2. **Exploratory Data Analysis (EDA)**
   - Understanding feature distributions
   - Identifying correlations and patterns

3. **Feature Engineering**
   - Encoding categorical variables
   - Scaling numerical features
   - Creating model-ready datasets

4. **Model Training**
   - Train-test split
   - Training multiple ML models

5. **Model Evaluation**
   - Comparing models using standard metrics
   - Selecting the best-performing model

6. **Prediction**
   - Making predictions on new or unseen data

---

## 🤖 Models & Evaluation

**Models Implemented:**
- Linear Regression
- Random Forest Regressor
- (Add any additional models if applicable)

**Evaluation Metrics:**
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The final trained model is saved as:
model.pkl


---

## 📁 Project Structure

student-performance-ml/
│
├── data/
│ ├── raw/
│ │ └── student_data.csv
│ └── processed/
│ ├── cleaned_data.csv
│ └── features.csv
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
├── README.md
├── LICENSE
└── .gitignore


---

## ⚙️ How to Run the Project

1. **Clone the repository**
```bash
git clone https://github.com/itskhyatii19/student-performance-ml.git
cd student-performance-ml
Install dependencies

pip install -r requirements.txt
Run the ML pipeline

python src/train_model.py
Make predictions

python src/predict.py
🧪 Key Learnings
Through this project, I gained hands-on experience in:

Building end-to-end machine learning pipelines

Applying feature engineering techniques to improve model performance

Evaluating and comparing multiple ML models

Structuring ML projects using modular, maintainable code

Working with real-world datasets and metrics

🚀 Future Improvements
Hyperparameter tuning for improved performance

Model deployment using FastAPI or Streamlit

Adding automated data validation

Experiment tracking using MLflow

👩‍💻 Author
Khyati Sharma
B.Tech in Artificial Intelligence
Interested in applied machine learning and data-driven problem solving

🔗 GitHub: https://github.com/itskhyatii19

⭐ If you find this project useful or insightful, feel free to star the repository!
