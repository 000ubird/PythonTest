'''
Created on 2018/08/27

@author: User
'''

from pandas import Series

if __name__ == '__main__':
    series = Series([1,2,3,4], index=["A","B","C","D"])
    print(series.index)     #Index(['A', 'B', 'C', 'D'], dtype='object')
    print(series.index[2:]) #Index(['C', 'D'], dtype='object')

    #Seriesのindexは書き換え不可
    #TypeError: Index does not support mutable operations
    #series.index[0] = "E"

    pass

