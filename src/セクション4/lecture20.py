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
    series1 = Series([0,1,2],   index=["A","B","C"])
    series2 = Series([3,4,5,6], index=["A","B","C","D"])
    print(series1+series2)
    '''
    A    3.0
    B    5.0
    C    7.0
    D    NaN    #Not a Number
    dtype: float64
    '''

    dframe1 = DataFrame(np.arange(4).reshape((2,2)), index=list("AB"),  columns=list("XY"))
    dframe2 = DataFrame(np.arange(9).reshape((3,3)), index=list("ABC"), columns=list("XYZ"))
    print(dframe1+dframe2)
    '''
    どちらかにしかないデータは全てNanになる
         X    Y   Z
    A  0.0  2.0 NaN
    B  5.0  7.0 NaN
    C  NaN  NaN NaN
    '''

    #もとのデータを入れたい場合
    print(dframe1.add(dframe2, fill_value=0))
    '''
         X    Y    Z
    A  0.0  2.0  2.0
    B  5.0  7.0  5.0
    C  6.0  7.0  8.0
    '''

    #SeriesとDataFrameの計算            X    Y    X
    series3 = dframe2.ix[2] #6.0  7.0  8.0
    print(dframe2)
    '''
       X  Y  Z
    A  0  1  2
    B  3  4  5
    C  6  7  8
    '''
    print(dframe2 - series3)    #series3が、dframe2の全行から引かれる
    '''
       X  Y  Z
    A -6 -6 -6
    B -3 -3 -3
    C  0  0  0

    '''
    pass
