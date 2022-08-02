import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture as GMM


def setup():
    df = pd.read_csv('input.csv')
    df_t = df['type']
    df.drop(['type'], axis=1, inplace=True)
    df_columns = df.columns.to_list()
    pca = PCA(.90, whiten=True)
    data = pca.fit_transform(df)
    gmm = GMM(n_components=3, covariance_type='full',
              random_state=45).fit(data)
    labels = gmm.predict(data)
    gmm = GMM(150, covariance_type='full', random_state=0)
    gmm.fit(data)
    data_new = gmm.sample(151)
    df_new = pca.inverse_transform(data_new[0])
    new_df = pd.DataFrame(df_new, columns=df_columns)
    new_df.to_csv('output.csv', index=True)
