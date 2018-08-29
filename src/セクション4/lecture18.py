'''
Created on 2018/08/27

@author: User
'''

import numpy as np
from numpy.random import randn
from pandas import Series, DataFrame
from pandas.tests.frame.test_validate import dataframe

if __name__ == '__main__':
    series = Series(np.arange(3), index=["a","b","c"])
    print(series)
    '''
    a    0
    b    1
    c    2
    '''
    print(series.drop("b")) #bの行が削除される
    '''
    a    0
    c    2
    dtype: int32
    '''

    #同様のことがDataFrameでも実行可能
    dframe1 = DataFrame(np.arange(9).reshape((3,3)), index=["a","b","c"], columns=["X","Y","Z"])
    print(dframe1)
    '''
       X  Y  Z
    a  0  1  2
    b  3  4  5
    c  6  7  8
    '''
    print(dframe1.drop("b", axis=0))    #bの行が削除される
    '''
       X  Y  Z
    a  0  1  2
    c  6  7  8
    '''

    print(dframe1.drop("Y", axis=1))    #「1」は列を表す

    #dframe1やseriesインスタンス自体は変更されていないので注意。


    pass
