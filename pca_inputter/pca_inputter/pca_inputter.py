import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

#url = "https://raw.githubusercontent.com/JWarmenhoven/ISLR-python/master/Notebooks/Data/USArrests.csv"

#USArrests = pd.read_csv(url)
#USArrests = USArrests.set_index('Unnamed: 0')

#X = USArrests.values
#n_omit = 20
#np.random.seed(15)
#ridx = np.random.choice(np.arange(X.shape[0]), n_omit, replace=False)
#cidx = np.random.choice(np.arange(X.shape[1]), n_omit, replace=True)
#Xna = X.copy()
#Xna[ridx, cidx] = np.nan


class PcaInputter:
    def __init__(self, data):

        if not isinstance(data, (pd.DataFrame, np.ndarray)):
            raise Exception("Input data must be a pandas DataFrame or a numpy array.")

        if isinstance(data, pd.DataFrame):
            if not all(data.applymap(np.isreal).all()):
                raise Exception("All values in the DataFrame must be numerical.")

            if data.apply(lambda row: row.isnull().all(), axis=1).any():
                raise Exception("Found a row where all columns are NaN in DataFrame.")

            if data.apply(lambda col: col.isnull().all(), axis=0).any():
                raise Exception("Found a column where all rows are NaN in DataFrame.")

            else:
                self.r_idx, self.c_idx = np.where(data.isnull())
                # self.raw_data = data.values

        if isinstance(data, np.ndarray):
            if not np.isreal(data).all():
                raise Exception("All values in the numpy array must be numerical.")

            if np.all(np.isnan(data), axis=1).any():
                raise Exception("Found a row where all columns are NaN in numpy array.")

            if np.all(np.isnan(data), axis=0).any():
                raise Exception("Found a column where all rows are NaN in numpy array.")

            else:
                self.r_idx, self.c_idx = np.where(np.isnan(data))
                # self.raw_data = data

        scaler = StandardScaler(with_std=True, with_mean=True)
        self.na_data = scaler.fit_transform(data)

    def run_pca(self, X, M=1):
        pca_obj = PCA().fit(X)
        self.scores = pca_obj.transform(X)
        self.components = pca_obj.components_

        return self.scores[:, 1 - M].reshape(50, M) @ self.components[:M][0].reshape(M, 4)
        # return L.dot(components[:M,:])

    def low_rank(self, X, M=1):
        U, D, V = np.linalg.svd(X)
        L = U[:, :M] * D[None, :M]
        return L.dot(V[:M])

    def iterfill(self):
        hat_data = self.na_data.copy()
        bar_data = np.nanmean(hat_data, axis=0)
        hat_data[self.r_idx, self.c_idx] = bar_data[self.c_idx]

        thresh = 1e-7
        rel_err = 1
        count = 0
        ismiss = np.isnan(self.na_data)
        mssold = np.mean(hat_data[~ismiss] ** 2)
        mss0 = np.mean(self.na_data[~ismiss] ** 2)
        mssold

        while rel_err > thresh:
            count += 1
            app_data = self.low_rank(hat_data, M=1)
            hat_data[ismiss] = app_data[ismiss]
            mss = np.mean(((self.na_data - app_data)[~ismiss]) ** 2)
            rel_err = (mssold - mss) / mss0
            mssold = mss
            # print(mssold,mss,mss0)
            print("Iteration: {0}, MSS:{1:.3f}, Rel.Err {2:.2e}".format(count, mss, rel_err))
        return hat_data


