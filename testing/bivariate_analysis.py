import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../Crop_recommendation.csv")

plt.figure(figsize=(12,6))
sns.scatterplot(
    data=df,
    x="humidity",
    y="temperature",
    hue="label",
    palette="tab20",
    legend=False
)

plt.title("Bivariate Analysis: Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.grid(True)

plt.show()