'''
Created on 2018/08/26

@author: User
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    arr = np.arange(5)
    print(arr)

    FILENAME1 = "arr_file"
    FILENAME2 = "arr_file2"
    FILENAME3 = "arr_file3"

    #バイナリで保存
    #拡張子をつけないと自動的に.npyになる
    np.save(FILENAME1, arr)

    #保存したファイルを読み込む
    arr2 = np.load(FILENAME1+".npy")
    print(arr2)

    #複数のarrayをzip形式で保存する
    #拡張子をつけないと自動的に.npzになる
    np.savez(FILENAME2, x=[1,2,3,4], y=[5,6,7,8])

    #保存したzipを読み込む
    zip_array = np.load(FILENAME2+".npz")
    print(zip_array['y'])   #[5 6 7 8] (名前でアクセス可能)

    #テキスト形式で保存
    #これは拡張子をつけてくれない
    array3 = np.arange(1,20)
    np.savetxt(FILENAME3+".txt", array3, delimiter=',')

    #保存したテキストを読み込む
    array4 = np.loadtxt(FILENAME3+".txt", delimiter=',')
    print(array4)

    pass

