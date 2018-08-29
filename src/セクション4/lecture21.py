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
    series1 = Series([10,40,30], index=["C","A","B"])
    print(series1)
    '''
    C    10
    A    40
    B    30
    dtype: int64
    '''

    #indexを使ってソート
    print(series1.sort_index())
    '''
    A    40
    B    30
    C    10
    dtype: int64
    '''

    #valueを使ってソート
    print(series1.sort_values())
    '''
    C    10
    B    30
    A    40
    dtype: int64
    '''

    #valueの各値が何番目に大きかを調べる
    print(series1.rank())
    '''
    C    1.0
    A    3.0
    B    2.0
    dtype: float64
    '''

    pass
