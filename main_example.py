import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

from pca_inputter import PcaInputter

url = "https://raw.githubusercontent.com/JWarmenhoven/ISLR-python/master/Notebooks/Data/USArrests.csv"

USArrests = pd.read_csv(url)
USArrests = USArrests.set_index('Unnamed: 0')


X = USArrests.values

n_omit = 20
np.random.seed(15)
ridx = np.random.choice(np.arange(X.shape[0]), n_omit, replace=False)
cidx = np.random.choice(np.arange(X.shape[1]), n_omit, replace=True)
Xna = X.copy()
Xna[ridx, cidx] = np.nan

scaler = StandardScaler(with_std=True, with_mean=True)
Xna = scaler.fit_transform(Xna)


inputter_object = PcaInputter(Xna)
Xinputted = inputter_object.iterfill()

print(Xna)
print("/n")
print(Xinputted)
