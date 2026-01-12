import pandas as pd
import joblib
import argparse

# Load model
model = joblib.load("model.pkl")

# Load feature columns
feature_cols = pd.read_csv("data/processed/features.csv").drop("G3", axis=1).columns

parser = argparse.ArgumentParser()
parser.add_argument("--g2", type=float, required=True)
parser.add_argument("--failures", type=int, required=True)
parser.add_argument("--famsup", type=str, required=True)
parser.add_argument("--medu", type=int, required=True)

args = parser.parse_args()

# Create empty input
input_df = pd.DataFrame(0, index=[0], columns=feature_cols)

# Fill known values
input_df["G2"] = args.g2
input_df["failures"] = args.failures
input_df["Medu"] = args.medu

if args.famsup.lower() == "yes":
    input_df["famsup_yes"] = 1

# Predict
pred = model.predict(input_df)[0]   # extract value first
pred = max(0, min(20, pred))        # clip
print("Predicted Final Grade:", round(pred, 2))
