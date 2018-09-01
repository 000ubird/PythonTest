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

'''
numpyで求めた回帰直線の誤差について
'''
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
    result = np.linalg.lstsq(A,y)  #いくつか返ってくる

    error_total = result[1]             #1番目の要素が、全ての点と回帰直線の距離の合計
    rmse = np.sqrt(error_total/len(A))  #平均二乗誤差(エラーの合計/点の数)の平方根

    '''
    標準正規分布によると、
    標準偏差の1倍までなら68%のデータが入っており、
    標準偏差の2倍までなら95%のデータが入る
    ※標準偏差は、分散の平方根
    下記の値は、標準偏差の値に該当するので、
    回帰直線で得られた式のの結果で、プラスマイナス2倍(6.60*2=13.2)の間に、全体のデータの95%が入る、ということが言える。
    この値は、回帰直線の式がどれくらいデータに当てはまっているかを定量的に表せる
    '''
    print('平均二乗誤差の平方根={:0.2f}'.format(rmse[0])) #6.60


    pass
