# Imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

# Calling datas
data = pd.read_csv("dataset/coin_Bitcoin.csv")

# Data Visualization
data.plot(x="Date", y="High")
plt.bar(x="Date", height="Height")
plt.show()

# Data Prediction