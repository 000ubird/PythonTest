'''
Created on 2018/09/02

@author: User
'''

import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import itertools

from pandas import Series,DataFrame
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#目的変数のaffairsの生データが0/1ではなく、
#不倫した時間を表しているので、した/しないに変換する関数
def affair_check(affairs):
    if affairs != 0:
        return 1    #した
    else:
        return 0    #しない

if __name__ == '__main__':
    #Affairs dataset
    #http://www.statsmodels.org/stable/datasets/generated/fair.html
    df = sm.datasets.fair.load_pandas().data
    print(df.head())
    '''
       rate_marriage   age    ...     occupation_husb   affairs
    0            3.0  32.0    ...                 5.0  0.111111
    1            3.0  27.0    ...                 4.0  3.230769
    2            4.0  22.0    ...                 5.0  1.400000
    3            4.0  37.0    ...                 5.0  0.727273
    4            5.0  27.0    ...                 4.0  4.666666
    '''

    df['Had_Affair'] = df['affairs'].apply(affair_check)

    ###データの前処理を行う
    #数字の大小に意味のないデータを「ダミー変数」という0/1で表すように変える
    #(例:職業はカテゴリごとに定数で表している)
    #pandasにget_dummies()というメソッドがあるので、これを使うと簡単にできる
    occ_dummies = pd.get_dummies(df['occupation'])
    occ_dummies.columns = ['occ1','occ2','occ3','occ4','occ5','occ6']
    hus_occ_dummies = pd.get_dummies(df['occupation_husb'])
    hus_occ_dummies.columns = ['hocc1','hocc2','hocc3','hocc4','hocc5','hocc6']

    #不要になったoccupationの列と、目的変数「Had_Affair」を削除して説明変数のデータフレームを生成
    X = df.drop(['occupation','occupation_husb','Had_Affair'], axis=1)
    X = df.drop(['Had_Affair'], axis=1)

    #2つのダミー変数のDataFrameを繋げる
    dummies = pd.concat([occ_dummies,hus_occ_dummies],axis=1)

    #ダミーのデータフレームと説明変数のデータフレームをつなげる
    X = pd.concat([X,dummies],axis=1)


    #Yに目的変数を保持する
    Y = df.Had_Affair
    Y = Y.values

    #多重共線性の変数の削除
    #ここでは、学生を表す「1」と、目的変数を削除する
#     X = X.drop('occ1',axis=1)
#     X = X.drop('hocc1',axis=1)
    X = X.drop('affairs',axis=1)


    #総当たりで学習用変数を選択
    max = 0
    max_list = []
    for combination_num in range(7,8):
        print(combination_num)
        list_comb = list(itertools.combinations(X.columns,combination_num))

        for list in list_comb:
            for i in range(0,len(list)):
                #print(X[list[i]].name)
                if i == 0:
                    X2 = X[list[i]]
                else :
                    X2 = pd.concat([X2,X[list[i]]],axis=1)

            #print("columns->",X2.columns)
            X_train, X_test, Y_train, Y_test = train_test_split(X2, Y, test_size=0.2)
            log_model2 = LogisticRegression()
            log_model2.fit(X_train, Y_train)
            class_predict = log_model2.predict(X_test)

            if max < metrics.accuracy_score(Y_test,class_predict):
                max = metrics.accuracy_score(Y_test,class_predict)
                max_list = list
                print("list->",list, ", Test Accuracy : ",metrics.accuracy_score(Y_test,class_predict))

        print("combi :", combination_num, "max Accuracy -> ", max, "max list -> ", max_list)

#     #学習と検査の実行
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
#     c_array = [1, 10,100,1000]
#     for c in c_array :
#         log_model2 = LogisticRegression(C=c)
#         log_model2.fit(X_train, Y_train)
#         print("{:>8} -> ".format(c),log_model2.score(X,Y)) #モデル精度の確認 0.7258875274897895
#
#     #検査
#     class_predict = log_model2.predict(X_test)
#     print("Test Accuracy : ",metrics.accuracy_score(Y_test,class_predict)) #0.7242462311557789

    pass

