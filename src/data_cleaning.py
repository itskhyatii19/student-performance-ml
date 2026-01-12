import pandas as pd

def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values (numeric)
    num_cols = df.select_dtypes(include="number").columns
    df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == "__main__":
    clean_data(
        "../data/raw/student_data.csv",
        "../data/processed/cleaned_data.csv"
    )
