import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../Crop_recommendation.csv")

# Select only numeric columns
numeric_cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="YlGnBu")
plt.title("Correlation Heatmap")
plt.show()

# Pair Plot
sns.pairplot(df[numeric_cols], diag_kind="hist")
plt.show()