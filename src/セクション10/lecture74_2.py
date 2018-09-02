'''
Created on 2018/09/01

@author: User
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn

from pandas import Series, DataFrame
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

sns.set_style("whitegrid")

'''
numpyで求めた回帰直線の誤差について
'''
if __name__ == '__main__':
    boston = load_boston()

    #データをDataFrame型に変換
    boston_df = DataFrame(boston.data)
    boston_df.columns = boston.feature_names
    boston_df['Price'] = boston.target

    lreg = LinearRegression()
    X_multi = boston_df.drop('Price',1) #説明変数
    Y_target= boston_df.Price           #目的変数

    print(X_multi.shape)    #(506, 13) -> 13個の説明変数×506データ
    print(Y_target.shape)   #(506,)

    #重回帰の回帰直線の式は下記
    #y = b+ a1*x1 + a2*x2 + a3*x3 + ... + an*xn
    lreg.fit(X_multi, Y_target) #回帰直線の作成
    print(lreg.intercept_)      #36.49110328036135 : y=ax+b のb(切片)に当たる数値
    print(len(lreg.coef_))      #13                : 係数の数は13個　重回帰は係数は複数

    coeff_df = DataFrame(boston_df.columns)
    coeff_df.columns = ['Features'] #列名に名前をつける
    coeff_df['Coefficient Estimate'] = pd.Series(lreg.coef_)    #重回帰の係数を保持
    print(coeff_df)
    '''
       Features  Coefficient Estimate
0      CRIM             -0.107171
1        ZN              0.046395
2     INDUS              0.020860
3      CHAS              2.688561
4       NOX            -17.795759
5        RM              3.804752
6       AGE              0.000751
7       DIS             -1.475759
8       RAD              0.305655
9       TAX             -0.012329
10  PTRATIO             -0.953464
11        B              0.009393
12    LSTAT             -0.525467
13    Price                   NaN
    '''

    pass
