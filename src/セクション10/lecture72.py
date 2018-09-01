'''
Created on 2018/09/01

@author: User
'''

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from sklearn.datasets import load_boston

sns.set_style("whitegrid")

if __name__ == '__main__':

    boston = load_boston()
    #print(boston.DESCR)     #データの説明を表示

    '''
    Data Set Characteristics:

        :Number of Instances: 506

        説明変数
        :Number of Attributes: 13 numeric/categorical predictive

        目的変数
        :Median Value (attribute 14) is usually the target

        :Attribute Information (in order):
            - CRIM     per capita crime rate by town
            - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
            - INDUS    proportion of non-retail business acres per town
            - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
            - NOX      nitric oxides concentration (parts per 10 million)
            - RM       average number of rooms per dwelling
            - AGE      proportion of owner-occupied units built prior to 1940
            - DIS      weighted distances to five Boston employment centres
            - RAD      index of accessibility to radial highways
            - TAX      full-value property-tax rate per $10,000
            - PTRATIO  pupil-teacher ratio by town
            - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
            - LSTAT    % lower status of the population
            - MEDV     Median value of owner-occupied homes in $1000's

        :Missing Attribute Values: None

        :Creator: Harrison, D. and Rubinfeld, D.L.

    This is a copy of UCI ML housing dataset.
    http://archive.ics.uci.edu/ml/datasets/Housing
    '''

    #目的変数を可視化
    #目的変数は「target」というフィールドに入っている
    plt.hist(boston.target, bins=100)   #binsは表示する棒の数
    plt.xlabel("Price($1,000)")
    plt.ylabel("Number of houses")
    plt.show()

    #説明変数を一部可視化
    PREDICTIVE_CRIM = 0
    PREDICTIVE_ZN   = 1
    PREDICTIVE_INDUS= 2
    PREDICTIVE_CHAS = 3
    PREDICTIVE_NOX  = 4
    PREDICTIVE_RM   = 5

    #横軸：部屋の数(説明変数) 縦軸：部屋の価格(目的変数)
    #説明変数は、「data」というフィールドに入っている
    plt.scatter(boston.data[:,PREDICTIVE_RM], boston.target)
    plt.ylabel("Price($1,000)")
    plt.xlabel("Number of rooms")
    plt.show()

    #データをDataFrame型に変換
    boston_df = DataFrame(boston.data)
    boston_df.columns = boston.feature_names
    print(boston_df.head())
    '''
          CRIM    ZN  INDUS  CHAS    NOX  ...    RAD    TAX  PTRATIO       B  LSTAT
    0  0.00632  18.0   2.31   0.0  0.538  ...    1.0  296.0     15.3  396.90   4.98
    1  0.02731   0.0   7.07   0.0  0.469  ...    2.0  242.0     17.8  396.90   9.14
    2  0.02729   0.0   7.07   0.0  0.469  ...    2.0  242.0     17.8  392.83   4.03
    3  0.03237   0.0   2.18   0.0  0.458  ...    3.0  222.0     18.7  394.63   2.94
    4  0.06905   0.0   2.18   0.0  0.458  ...    3.0  222.0     18.7  396.90   5.33
    '''

    #データ(Price列)の追加
    boston_df['Price'] = boston.target
    print(boston_df.head())
    '''
          CRIM    ZN  INDUS  CHAS  ...    PTRATIO       B  LSTAT  Price
    0  0.00632  18.0   2.31   0.0  ...       15.3  396.90   4.98   24.0
    1  0.02731   0.0   7.07   0.0  ...       17.8  396.90   9.14   21.6
    2  0.02729   0.0   7.07   0.0  ...       17.8  392.83   4.03   34.7
    3  0.03237   0.0   2.18   0.0  ...       18.7  394.63   2.94   33.4
    4  0.06905   0.0   2.18   0.0  ...       18.7  396.90   5.33   36.2
    '''

    #seabornを使用し、回帰直線を引いて、散布図を示す
    sns.lmplot("RM", "Price", data = boston_df)
    plt.show()

    pass
