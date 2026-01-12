# Student Performance Prediction – End-to-End ML Project

This project demonstrates a complete machine learning pipeline to predict student performance using real-world data.

The goal is to showcase:
- Proper project structure
- Clean data preprocessing
- Feature engineering
- Model training
- Evaluation using standard metrics

This repository is built as a **portfolio project** to demonstrate practical ML skills.

---

## Project Structure

student-performance-ml/
│
├── data/
│   └── student_data.csv
│
├── src/
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   └── evaluation.py
│
├── requirements.txt
└── README.md

---

## Dataset

- Source: Kaggle – Student Performance Dataset  
- Rows: ~3000  
- Columns: Academic and lifestyle factors  
- Target Variable: **Performance Index**

---

## Pipeline Overview

1. **Data Cleaning**
   - Remove duplicates
   - Handle missing values
   - Fix data types

2. **Feature Engineering**
   - Select relevant features
   - Create derived features
   - Encode categorical variables

3. **Model Training**
   - Train/Test split
   - Linear Regression model
   - (Later upgrades planned)

4. **Evaluation**
   - Mean Absolute Error (MAE)
   - R² Score
   - Visualizations

---

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
