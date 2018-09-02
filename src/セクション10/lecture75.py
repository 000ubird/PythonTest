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

    X_multi = boston_df.drop('Price',1) #説明変数
    Y_target= boston_df.Price           #目的変数

    #学習用データと検証用データを保持
    #X_train : 学習用の説明変数
    #X_test  : テスト用の説明変数
    #Y_train : 学習用の目的変数
    #Y_test  : テスト用の目的変数
    #
    #train_test_split()に説明変数と目的変数を入れると、
    #上記の4つのデータに分けてくれる
    #データのサイズは変わらないが、実行するたびに選ばれるデータは変わる
    #https://stackoverflow.com/questions/46572475/module-sklearn-has-no-attribute-cross-validation
    X_train, X_test, Y_train, Y_test = sklearn.model_selection.train_test_split(X_multi, boston_df.Price)
    print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape) #(379, 13) (127, 13) (379,) (127,)

    lreg = LinearRegression()
    lreg.fit(X_train, Y_train)

    pred_train = lreg.predict(X_train)  #学習用に使用したデータをもとに出した目的変数 こちらのほうが誤差が少ない
    pred_test  = lreg.predict(X_test)   #学習用には使用していないデータで出した目的変数

    #誤差を求める
    #学習用の目的変数(正解) と学習データから算出した目的変数(予測値)の平均二乗誤差を出す
    print(np.mean((Y_train - pred_train) **2))  #19.726803029252423

    #テスト用データを使って出した結果の平均二乗誤差
    print(np.mean((Y_test - pred_test) **2))  #30.28264211069599

    # 学習用データの残差プロット
    train = plt.scatter(pred_train, (pred_train - Y_train), c='b', alpha=0.5)

    # テスト用データの残差プロット
    test = plt.scatter(pred_test, (pred_test - Y_test), c='r', alpha=0.5)

    #y=0の水平な線を描いておく
    #残差プロットのデータがこのy=0の直線に近ければ、良いモデルができたことになる
    plt.hlines(y=0, xmin=-10, xmax=50)

    plt.legend((train,test), ('Training','Test'), loc='lower left')
    plt.title('Residual Plots')
    plt.show()

    pass
