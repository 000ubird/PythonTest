'''
Created on 2018/08/13

@author: User
'''

import numpy as np
from numpy import int64

if __name__ == '__main__':
    #通常のリスト
    my_list1 = [1,2,3,4]
    my_list2 = ["a","b","c","d"]

    #多次元配列
    my_lists = [my_list1,my_list2]
    print(my_lists)

    #numpyの配列 同じ型のみ生成可能
    np_list = np.array(my_list1)
    print(np_list)
    print(np_list.dtype)    #int32

    #すべての要素が0の行列
    np_zeros = np.zeros(5)
    print(np_zeros)
    print(np_zeros.dtype)   #float64

    #すべての要素が1の行列
    np_ones = np.ones((5,5), dtype = int64)
    print(np_ones)
    print(np_ones.shape)

    #空
    np_empty = np.empty((4,6))
    print(np_empty)

    #単位行列
    np_eye = np.eye(5)
    print(np_eye)

    #arange
    np_arange = np.arange(5,50,2)
    print(np_arange)    #5 7 9 11 13 ...

    pass

