import pandas as pd

def engineer_features(input_path, output_path):
    df = pd.read_csv(input_path)

    # Drop target leakage columns
    if "G3" in df.columns:
        y = df["G3"]
        df = df.drop("G3", axis=1)

    # One-hot encode categoricals
    df = pd.get_dummies(df, drop_first=True)

    # Add target back
    df["G3"] = y

    df.to_csv(output_path, index=False)
    print("Features saved to:", output_path)


if __name__ == "__main__":
    engineer_features(
        "data/processed/cleaned_data.csv",
        "data/processed/features.csv"
    )
