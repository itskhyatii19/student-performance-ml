import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

# Load data
df = pd.read_csv("data/processed/features.csv")

X = df.drop("G3", axis=1)
y = df["G3"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model (regularized)
model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, preds))
print("R2:", r2_score(y_test, preds))

# Save model
joblib.dump(model, "model.pkl")
print("Model saved.")

coef_df = pd.DataFrame({
    "Feature": X.columns,
    "Weight": model.coef_
}).sort_values(by="Weight", ascending=False)

print(coef_df.head(10))
