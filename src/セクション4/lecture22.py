'''
Created on 2018/09/01

@author: User
'''

import numpy as np
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

#https://note.nkmk.me/python-pandas-datareader-stock-population/
#http://clubknot.net/?p=1666
#panda_datareaderを使用するときにやること
import pandas_datareader.data as pd_data

from pandas import DataFrame

if __name__ == '__main__':
    dframe1 = DataFrame(np.arange(9).reshape((3,3)), index=list("ABC"), columns=list("XYZ"))

    #データの色々な統計情報を返してくれるメソッド
    #便利
    print(dframe1.describe())
    '''
    X    Y    Z
    count  3.0  3.0  3.0
    mean   3.0  4.0  5.0
    std    3.0  3.0  3.0
    min    0.0  1.0  2.0
    25%    1.5  2.5  3.5
    50%    3.0  4.0  5.0
    75%    4.5  5.5  6.5
    max    6.0  7.0  8.0
    '''

    #Web上からデータを取得する
    start = datetime.datetime(2014,1, 1)
    end   = datetime.datetime(2018,8,31)

    #Webから様々なデータを取得してくれるメソッド
    #https://iextrading.com/apps/stocks/
    f = pd_data.DataReader(['BABA', 'AAPL', 'FB'], "iex", start ,end)
    print(f['BABA'].head())
    print(f['BABA'].tail())

    print(f['AAPL'].head())
    print(f['AAPL'].tail())
    '''
    open     high      low    close     volume
    date
    2014-01-02  73.1096  73.2873  72.6282  72.7741   58791957
    2014-01-03  72.7386  72.8491  71.1032  71.1756   98303870
    2014-01-06  70.7112  71.9413  70.2046  71.5637  103359151
    2014-01-07  71.6150  71.8308  70.7737  71.0516   79432766
    2014-01-08  70.8901  71.7782  70.8743  71.5019   64686685
                  open    high     low   close    volume
    date
    2018-08-27  217.15  218.74  216.33  217.94  20525117
    2018-08-28  219.01  220.54  218.92  219.70  22776766
    2018-08-29  220.15  223.49  219.41  222.98  27254804
    2018-08-30  223.25  228.26  222.40  225.03  48793824
    2018-08-31  226.51  228.87  226.00  227.63  43340134
    '''

#     f['BABA'].high.plot()
#     f['BABA'].low.plot()
#     f['AAPL']['high'].plot()
#     f['AAPL']['low'].plot(grid=True)
#     plt.show()
#     plt.savefig('testfig')

    data2 = DataFrame(None, index=f['BABA'].index, columns=['BABA', 'AAPL', 'FB'])
    data2["BABA"] = f['BABA'].high
    data2["AAPL"] = f['AAPL'].high
    data2["FB"]   = f['FB'].high

    data2.plot()
    plt.show()

    #相関関係を調べる
    print(data2.corr())
    sns.heatmap(data2.corr())
    plt.show()
    pass
