# Student Performance Prediction – End-to-End ML Project

This project demonstrates a complete machine learning pipeline to predict student final grades using real-world educational data.

The **Actual vs Predicted** plot shows strong alignment along the diagonal, confirming good model accuracy and low prediction error.

This repository is built as a **portfolio project** to showcase practical machine learning skills and clean project structuring.

---

## Project Structure

student-performance-ml/
│
├── data/
│   ├── raw/
│   │   └── student_data.csv
│   ├── processed/
│   │   ├── cleaned_data.csv
│   │   └── features.csv
│
├── src/
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluation.py
│   └── predict.py
│
├── model.pkl
├── requirements.txt
└── README.md

---

## Dataset

- Source: Kaggle – Student Performance Dataset  
- Rows: ~395  
- Columns: Academic + lifestyle factors  
- Target Variable: **Final Grade (G3)**  

---

## Pipeline Overview

### 1. Data Cleaning
- Remove duplicate rows  
- Handle missing numeric values  
- Save cleaned dataset  

### 2. Exploratory Data Analysis (EDA)
- Grade distributions  
- Correlation analysis  
- Key feature trends  

### 3. Feature Engineering
- One-hot encoding of categorical variables  
- Feature selection  
- Save engineered features  

### 4. Model Training
- Train/Test split  
- Ridge Regression  
- Model persistence using joblib  

### 5. Evaluation
- Mean Absolute Error (MAE)  
- R² Score  
- Actual vs Predicted visualization  

---

## Model Performance

- **MAE:** ~0.95  
- **R² Score:** ~0.83  

This indicates strong predictive performance.

---

## Key Insights

- Previous exam score (**G2**) is the strongest predictor.
- Family support positively affects performance.
- Parental profession has measurable impact.
- Students from urban areas perform slightly better.

Top weighted features were extracted from Ridge Regression coefficients.

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

2. Run data cleaning
python src/data_cleaning.py

3. Feature engineering
python src/feature_engineering.py

4. Train model
python src/train_model.py

5. Evaluate model
python src/evaluation.py

6. Make prediction
python src/predict.py --g2 15 --failures 0 --famsup yes --medu 4

Tech Stack

Python

Pandas

NumPy

Matplotlib

Scikit-learn

Future Improvements

Try tree-based models

Hyperparameter tuning

Deploy as a web app

Add cross-validation

Author

Khyati Sharma
Aspiring Machine Learning Engineer