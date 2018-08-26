'''
Created on 2018/08/13

@author: User
'''

import numpy as np

if __name__ == '__main__':
    ary = np.array([[1,2,3,4],[6,7,8,9]])

    print(ary * ary)
    print(ary - ary)
    print(1 - ary)

    #それぞれの要素を3乗
    print(ary ** 3)

    pass

