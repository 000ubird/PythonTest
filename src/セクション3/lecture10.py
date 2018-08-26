'''
Created on 2018/08/26

@author: User
'''

import numpy as np

if __name__ == '__main__':
    array = np.arange(1,10)         #[1 2 3 4 5 6 7 8 9]
    array = array.reshape((3,3))    #[[1 2 3]
                                    # [4 5 6]
                                    # [7 8 9]]

    #転置行列の作成
    array = array.T                 #[[1 4 7]
                                    # [2 5 8]
                                    # [3 6 9]]
    #行列の入れ替え
    array = array.transpose((0,1))

    #行列の掛け算(内積)
    array = np.arange(1,10).reshape((3,3))
    array2 = np.dot(array, array.T)
    '''
    [[ 14  32  50]    1*1+2*2+3*3=14 1*4+2*5+3*6=32
     [ 32  77 122]
     [ 50 122 194]]
    '''

    #3次元配列
    #イメージ：i*jの行列がk個積み上がっているイメージ
    array_3d = np.arange(12).reshape(3,2,2)  #2*2行列*3

    '''
    [[[ 0  1]
      [ 2  3]]

     [[ 4  5]
      [ 6  7]]

     [[ 8  9]
      [10 11]]]
    '''

    print(array_3d)
    pass

