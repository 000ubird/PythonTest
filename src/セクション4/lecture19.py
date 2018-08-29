'''
Created on 2018/08/27

@author: User
'''

import numpy as np
from numpy.random import randn
from pandas import Series, DataFrame
from pandas.tests.frame.test_validate import dataframe
from bokeh.layouts import column

if __name__ == '__main__':
    #Seriesについてのデータの取り出し方
    series = Series(np.arange(3), index=["A","B","C"])
    series = 2 * series
    print(series)
    '''
    A    0
    B    2
    C    4
    dtype: int32
    '''

    print(series["B"], series[1])               #2  2
    print(series[1:],"\n", series[["B","C"]])
    series[series>3] = 10   #3以上の値に10を代入
    print(series)
    '''
    A     0
    B     2
    C    10
    dtype: int32
    '''

    #DataFrameについてのデータの取り出し方
    dframe = DataFrame(np.arange(9).reshape((3,3)), index=["A","B","C"], columns=["X","Y","Z"])
    print(dframe)
    '''
       X  Y  Z
    A  0  1  2
    B  3  4  5
    C  6  7  8
    '''
    #列方向へのアクセス
    print(dframe["X"])
    print(dframe[dframe["Y"]>3])
    print(dframe>3)
    '''
           X      Y      Z
    A  False  False  False
    B  False   True   True
    C   True   True   True
    '''

    #行方向へのアクセス
    print(dframe.ix["A"])
    '''
    X    0
    Y    1
    Z    2
    Name: A, dtype: int32
    '''

    pass
