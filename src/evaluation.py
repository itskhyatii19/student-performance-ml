import pandas as pd
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv("data/processed/features.csv")
X = df.drop("G3", axis=1)
y = df["G3"]

model = joblib.load("model.pkl")
preds = model.predict(X)

plt.scatter(y, preds)
plt.xlabel("Actual Grades")
plt.ylabel("Predicted Grades")
plt.title("Actual vs Predicted")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.show()

print("MAE:", mean_absolute_error(y, preds))
print("R2:", r2_score(y, preds))
