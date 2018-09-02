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

    ###各データについて簡単に分析するため、可視化をする

    #不倫をした/しないを簡単にグループ分け
    print(df.groupby('Had_Affair').mean())

    #年齢データをもとにヒストグラム化
    sns.countplot('age', data=df.sort_values(by='age'), hue='Had_Affair', palette='coolwarm')
    plt.show()

    #結婚から経過した年数をもとにヒストグラム化
    sns.countplot('yrs_married', data=df.sort_values(by='yrs_married'), hue='Had_Affair', palette='coolwarm')
    plt.show()

    #子供の数をもとにヒストグラム化
    sns.countplot('children', data=df.sort_values(by='children'), hue='Had_Affair', palette='coolwarm')
    plt.show()

    #学歴
    sns.countplot('educ', data=df.sort_values(by='educ'), hue='Had_Affair', palette='coolwarm')
    plt.show()

    ###データの前処理を行う
    #数字の大小に意味のないデータを「ダミー変数」という0/1で表すように変える
    #(例:職業はカテゴリごとに定数で表している)
    #pandasにget_dummies()というメソッドがあるので、これを使うと簡単にできる
    occ_dummies = pd.get_dummies(df['occupation'])
    occ_dummies.columns = ['occ1','occ2','occ3','occ4','occ5','occ6']
    hus_occ_dummies = pd.get_dummies(df['occupation_husb'])
    hus_occ_dummies.columns = ['hocc1','hocc2','hocc3','hocc4','hocc5','hocc6']

    print(occ_dummies.head())
    '''
       occ1  occ2  occ3  occ4  occ5  occ6
    0     0     1     0     0     0     0
    1     0     0     1     0     0     0
    2     0     0     1     0     0     0
    3     0     0     0     0     1     0
    4     0     0     1     0     0     0
    '''

    #不要になったoccupationの列と、目的変数「Had_Affair」を削除して説明変数のデータフレームを生成
    X = df.drop(['occupation','occupation_husb','Had_Affair'], axis=1)

    #2つのダミー変数のDataFrameを繋げる
    dummies = pd.concat([occ_dummies,hus_occ_dummies],axis=1)

    #ダミーのデータフレームと説明変数のデータフレームをつなげる
    X = pd.concat([X,dummies],axis=1)
    print(X.head())
    '''
       rate_marriage   age  yrs_married  children  ...    hocc3  hocc4  hocc5  hocc6
    0            3.0  32.0          9.0       3.0  ...        0      0      1      0
    1            3.0  27.0         13.0       3.0  ...        0      1      0      0
    2            4.0  22.0          2.5       0.0  ...        0      0      1      0
    3            4.0  37.0         16.5       4.0  ...        0      0      1      0
    4            5.0  27.0          9.0       1.0  ...        0      1      0      0
    5            4.0  27.0          9.0       0.0  ...        0      1      0      0
    '''

    #Yに目的変数を保持する
    Y = df.Had_Affair
    Y = Y.values

    #多重共線性の変数の削除
    #ここでは、学生を表す「1」と、目的変数を削除する
    X = X.drop('occ1',axis=1)
    X = X.drop('hocc1',axis=1)
    X = X.drop('affairs',axis=1)

    ###ここからロジスティック回帰
    log_model = LogisticRegression()
    log_model.fit(X,Y)          #モデルの生成
    print(log_model.score(X,Y)) #モデル精度の確認 0.7258875274897895

    #目的変数Yの平均値を計算し、精度と比較する 0.3224945020420987
    #1 - 0.32 = 0.68
    print(Y.mean())

    ###どの説明変数が予測に寄与しているかを確認
    coeff_df = DataFrame([X.columns, log_model.coef_[0]]).T
    print(coeff_df)

    '''
                    0           1
    0   rate_marriage   -0.697885
    1             age   -0.056347
    2     yrs_married    0.103906
    3        children   0.0181728
    4       religious   -0.368496
    5            educ  0.00878983
    6            occ2    0.297979
    7            occ3    0.607916
    8            occ4    0.346038
    9            occ5    0.942365
    10           occ6    0.905324
    11          hocc2    0.218433
    12          hocc3    0.324312
    13          hocc4    0.188145
    14          hocc5    0.211584
    15          hocc6    0.214427
    '''

    #学習と検査の実行
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    log_model2 = LogisticRegression()
    log_model2.fit(X_train, Y_train)

    #検査
    class_predict = log_model2.predict(X_test)
    print(metrics.accuracy_score(Y_test,class_predict)) #0.7242462311557789

    pass

