# PCA_data_inputter
This is a powerful technique for handling missing values in numerical datasets.

The algorithm is referred to as “Hard-Impute” in Mazumder, Hastie, and Tibshirani (2010) 
“Spectral regularization algorithms for learning large incomplete matrices”, published in Journal of 
Machine Learning Research, pages 2287–2322.

The algorithm is published at PYPI https://pypi.org/project/pca-inputter/

Usage:
- pip install the pca_inputter package
- initialize the class PcaInputter(df), where df is your dataset with missing values
- call the iterfill(M, thresh) method of the PcaInputter object. 

Note: 
The number of principal components M used for reconstructing the missing values is defaulted to 1, 
but can be specified to any M<=p. The algorithm stops once the change in values between 2 iterations 
is below the threshold. The threshold is defaulted to thresh=1e-7, but can be changed.

In addition, a IPYNB notebook provides a couple of test datasets.

