'''
Created on 2018/08/27

@author: User
'''

import pandas as pd
from pandas import Series
from zmq.utils.constant_names import new_in

if __name__ == '__main__':
    series = Series([3,6,9,12])
    print(series)

    #Seriesでは、各要素にindexという名前がついている
    '''
    0     3
    1     6
    2     9
    3    12
    dtype: int64
    '''

    print(series.values)    #[ 3  6  9 12] ※numpyのarrayになっている
    print(series.index)     #RangeIndex(start=0, stop=4, step=1)

    data = Series([100,200,300], index=['apple', 'banana', 'orange'])
    print(data)
    '''
    apple     100
    banana    200
    orange    300
    dtype: int64
    '''

    #個別データにアクセス
    print(data['banana'])   #200

    #200以上のものだけを出す
    print(data[data>=200])
    '''
    banana    200
    orange    300
    dtype: int64
    '''

    #data>=200 の中身
    print(data>=200)
    '''
    apple     False
    banana     True
    orange     True
    dtype: bool
    '''

    #pythonの辞書型のような使い方も可能
    print('orange' in data) #True

    #pythonの辞書型⇔Seriesの相互変換が可能
    data_dict = data.to_dict()
    print(data_dict)            #{'apple': 100, 'banana': 200, 'orange': 300}

    data2 = Series(data_dict)
    print(data2)
    '''
    apple     100
    banana    200
    orange    300
    dtype: int64
    '''

    #indexを指定して新たにSeriesを作ることもできる
    new_index = ['apple','banana','orange','hoge']
    data3 = Series(data, index=new_index)
    print(data3)
    '''
    apple     100.0
    banana    200.0
    orange    300.0
    hoge        NaN indexにない要素はnullが入る
    dtype: float64

    '''

    print(pd.isnull(data3))     #nullの所だけTrue
    print(pd.notnull(data3))    #nullでないところがTrue

    data3.name       = "oyatsu no onedan"   #Series全体に名前をつけることができる
    data3.index.name = "oyatsu no namae"    #indexに名前をつけることもできる

    pass
