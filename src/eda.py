import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned data
df = pd.read_csv("../data/processed/cleaned_data.csv")

print("\nDataset shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nMissing values:\n", df.isnull().sum())

# Summary statistics
print("\nStatistical summary:\n", df.describe())

# Distribution of target
plt.figure()
sns.histplot(df["G3"], kde=True)
plt.title("Final Grade Distribution (G3)")
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=False, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()
