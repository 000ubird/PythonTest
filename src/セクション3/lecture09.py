'''
Created on 2018/08/13

@author: User
'''

import numpy as np

if __name__ == '__main__':
    array = np.arange(0,10) #[ 0  1  2  3  4  5  6  7  8  9]

    print(array[1:5])       #[1 2 3 4]
    array[0:4] = 100
    print(array[0:13])      #[100 100 100 100   4   5   6   7   8   9]

    #参照渡し
    array = np.arange(0,10)
    array2 = array[1:5]
    array2[:] = 99  #すべての要素
    print(array2)   #[99 99 99 99]
    print(array)    #[ 0 99 99 99 99  5  6  7  8  9]

    #値渡し
    array = np.arange(0,10)
    array2 = array.copy()   #配列のコピーはこれを使うこと
    array2[:] = 99
    print(array2)   #[99 99 99 99 99 99 99 99 99 99]
    print(array)    #[0 1 2 3 4 5 6 7 8 9]

    #多次元配列の参照
    #1 2 3
    #4 5 6
    #7 8 9
    array_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print(array_2d[1])      #[4 5 6]
    print(array_2d[1,:])    #[4 5 6]
    print(array_2d[2][2])   #9
    print(array_2d[2,2])    #9
    print(array_2d[:2,1:])  #[[2 3]
                            # [5 6]]

    array_2d = np.zeros((10,10))
    arr_length = array_2d.shape[1]
    print(arr_length)   #10

    for i in range(arr_length):
        for j in range(arr_length):
            array_2d[i][j] = i+j

    print(array_2d)

    #順番を変えて、任意の行を取り出す
    print(array_2d[[6,4,2]])

    pass

