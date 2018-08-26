'''
Created on 2018/08/26

@author: User
'''

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    points = np.arange(-5, 5, 0.01)
    dx, dy = np.meshgrid(points, points)
    print(points)

    #グラフを描画
    plt.imshow(dx)
    plt.show()
    plt.imshow(dy)
    plt.show()

    z = (np.sin(dx) + np.sin(dy))
    plt.imshow(z)
    plt.colorbar()
    plt.title("Plot for sin(x)+sin(y)")
    plt.show()

    #リスト内包表記
    A = np.array([1,2,3,4])
    B = np.array([100,200,300,400])
    condition = np.array([True, True, False, False])

    #aにはA、bにはB、condにはconditionの内容が入る
    #1つ1つの要素に対し、condがTrueならa、Falseならbが入る
    #これは多次元の配列に対応できず、速度も遅い
    answer = [(a if cond else b) for a,b,cond in zip(A,B,condition)]
    print(answer)                       #リストが返ってくる    [1, 2, 300, 400]

    #こっちを使うと良い。多次元配列も対応可能
    #conditionがTrueならAの要素、FaulseならBの要素を選ぶ
    answer2 = np.where(condition, A, B) #arrayが返ってくる[  1   2 300 400]
    print(answer2)

    #5行5列のランダムな要素が入っている配列から、条件に合うものを選ぶ
    rand_array = np.random.randn(5,5)
    print(np.where(rand_array < 0, 0, rand_array))

    #便利な関数
    ary = np.array([[1,2,3], [4,5,6], [7,8,9]])
    bool= np.array([True, False, True])
    print(ary.sum())    #45
    print(ary.sum(0))   #[12 15 18] (列方向に足す)
    print(ary.mean())   #5.0 (平均)
    print(ary.std())    #2.581988897471611 (標準偏差)
    print(ary.var())    #6.666666666666667 (分散)
    #https://sci-pursuit.com/math/statistics/standard-deviation.html
    print(bool.any())   #1つでもTrueがあればTrue
    print(bool.all())   #全てがFaulseならFalse

    #ソート
    rand_array = np.random.randn(5,5)
    rand_array.sort()   #配列の中身がソートされるので、代入の必要なし
    print(rand_array)

    #重複をなくす
    str_array = np.array(["aaa", "bbb", "aaa", "ddd", "bbb", "ddd"])
    print(np.unique(str_array)) #['aaa' 'bbb' 'ddd']

    #指定した要素が配列内に含まれるかを調べる
    print(np.in1d(["aaa", "bbb", "ccc"], str_array))    #[ True  True False]

    pass

