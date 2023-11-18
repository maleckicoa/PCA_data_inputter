pca_inputter is a powerful technique for handling missing values in numerical datasets

The algorithm is referred to as “Hard-Impute” in Mazumder, Hastie, and Tibshirani (2010) “Spectral 
regularization algorithms for learning large incomplete matrices”, published in Journal of Machine 
Learning Research, pages 2287–2322. 

The algorithm first replaces the missing values with column averages, in order to have a complete matrix.
The dataframe is then decomposed into principal component scores and loading vectors. These are multiplied 
in order to reconstruct the missing values of the dataframe. The decomposition is done again and the 
missing values are replaced iteratively until there is no material change in the values between 2 iterations.

Usage:After importing the package, initialize the class PcaInputter(df), where df is your dataset with missing 
values. Note that the dataset must be either a numpy array or a pandas dataframe, and that all features must
be numerical.

To run the algorithm, call the iterfill(M, thresh) method of the PcaInputter object.
The number of principal components M used for reconstructing the missing values is defaulted to 1, but can be
specified to any M<=p. The algorithm stops once the change between the values between 2 iterations is below 
the threshold. The threshold is defaulted to thresh=1e-7, but can be changed.
