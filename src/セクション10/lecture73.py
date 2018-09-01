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

    #データをDataFrame型に変換
    boston_df = DataFrame(boston.data)
    boston_df.columns = boston.feature_names
    boston_df['Price'] = boston.target

    #回帰直線をnumpyを使って求める
    #https://ja.wikipedia.org/wiki/%E7%B7%9A%E5%BD%A2%E5%9B%9E%E5%B8%B0
    #今回は単回帰なので、回帰直線は下記の式で求められる
    # 回帰直線の式：y=ax+b
    # 書き換えると、下記の様になる
    # A = [x, 1]
    # p = [a]
    #     [b]
    # y = Ap で求められる

    #上記のAを作る
    A = boston_df.RM             #1行506列のデータ
    A = np.vstack(boston_df.RM)  #506行1列のデータ
    print(A.shape)               #(506, 1)
    A = np.array([ [value, 1] for value in A ] )    #リスト内包表記

    #上記のyを作る
    y = boston_df.Price
    print(y.shape)

    #上記のpのaとbを求める
    #least squere （最小二乗法）
    a, b = np.linalg.lstsq(A,y)[0]  #いくつか返ってくる

    #求めた回帰直線をプロット
    x = boston_df.RM
    plt.plot(boston_df.RM, boston_df.Price, 'o')
    plt.plot(x, a*x+b, 'r') #y = ax+b
    plt.show()

    #回帰直線を使って目的変数を求める
    room_num = 7
    target = a * room_num + b
    print(target)   #29.044142091823623

    pass
