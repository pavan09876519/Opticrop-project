import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("../Crop_recommendation.csv")

# Features
cols = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

# Create boxplots
plt.figure(figsize=(16,8))

for i, col in enumerate(cols, 1):
    plt.subplot(2, 4, i)
    sns.boxplot(y=df[col], color="lightgreen")
    plt.title(col)

plt.suptitle("Box Plot", fontsize=16)
plt.tight_layout()
plt.show()