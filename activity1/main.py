# Imports
import pandas as pd, numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing

# Calling datas
data = pd.read_csv("dataset/coin_Bitcoin.csv")

# Data Visualization

data.plot(x="Date", y="High")
plt.bar(x="Date", height="Height")
plt.show()

# Data Prediction
