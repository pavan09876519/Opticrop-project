import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Crop_recommendation.csv")

cols = ["N","P","K","temperature","humidity","ph","rainfall"]

plt.figure(figsize=(15,8))

for i, col in enumerate(cols,1):
    plt.subplot(3,3,i)
    sns.histplot(df[col], kde=True, color="green")
    plt.title(f"Distribution of {col}")

plt.tight_layout()
plt.show()