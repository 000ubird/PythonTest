'''
Created on 2018/08/27

@author: User
'''

from numpy.random import randn
from pandas import Series, DataFrame

if __name__ == '__main__':
    data1 = Series([1,2,3,4], index=["A","B","C","D"])
    data2 = data1.reindex(["A","B","C","D","E","F"], fill_value=0)

    print(data1)
    '''
    A    1
    B    2
    C    3
    D    4
    dtype: int64
    '''

    print(data2)
    '''
    A    1
    B    2
    C    3
    D    4
    E    0    追加したところがfill_valueによって埋まる
    F    0
    dtype: float64
    '''

    data3 = Series(["A","B","C"], index=[0,5,10])
    data3 = data3.reindex(range(15), method='ffill')    #forward fill
    print(data3)
    '''
    0     A
    1     A
    2     A
    3     A
    4     A
    5     B
    6     B
    7     B
    8     B
    9     B
    10    C
    11    C
    12    C
    13    C
    14    C
    dtype: object
    '''

    dframe = DataFrame(randn(25).reshape((5,5)), index=["A","B","C","D","E"], columns=["col1","col2","col3","col4","col5"])
    print(dframe)
    '''
           col1      col2      col3      col4      col5
    A -0.183026  0.298772  0.327232 -2.582834  1.104827
    B  0.922415 -0.178733  0.106850  0.060173 -1.997644
    C -1.841675 -0.385489  0.863282 -1.160615  0.545738
    D  0.614787 -1.184005  0.125622 -0.112098  0.588512
    E  0.190054 -1.390058  0.026141 -0.727808  0.174224
    '''

    #行の追加
    new_index = ["A","B","C","D","E","F"]
    dframe2 = dframe.reindex(new_index)
    print(dframe2)
    '''
           col1      col2      col3      col4      col5
    A -0.776007 -0.867861  2.478000  1.534051  0.176876
    B -1.146955  1.557304  0.829215  0.933322  0.726945
    C  0.725432  1.053244  0.030513 -0.359150  0.179655
    D -0.974802 -0.841037  0.546601  0.806764  1.047738
    E -0.619140  1.001950  1.636064 -0.333991  1.164419
    F       NaN       NaN       NaN       NaN       NaN
    '''

    #列の追加
    new_columns = ["col1","col2","col3","col4","col5","col6"]
    dframe3 = dframe.reindex(columns=new_columns)
    print(dframe3)
    '''
           col1      col2      col3      col4      col5  col6
    A -0.358404 -0.632142  0.224087 -1.559911  0.488201   NaN
    B  0.117307  1.781615 -1.045211  0.657583 -1.486705   NaN
    C  0.824834 -0.018770  0.050063 -0.040765  1.752814   NaN
    D -0.179507  0.393456  0.900704  1.307103 -1.741242   NaN
    E -0.163492  1.604415  1.592163  0.963146 -1.410337   NaN
    '''

    #行列を一気に追加
    print(dframe.ix[new_index, new_columns])
    '''
           col1      col2      col3      col4      col5  col6
    A -0.512337 -0.262989 -1.219498  2.213791  0.513712   NaN
    B  0.676878  0.606967  1.192244 -0.871140  0.654473   NaN
    C  0.259311 -0.173896 -0.465250  0.118614 -1.030224   NaN
    D -0.744654  0.784790  0.481306  1.856533  0.557846   NaN
    E  0.179032 -0.677668 -0.250094  1.178341  1.255734   NaN
    F       NaN       NaN       NaN       NaN       NaN   NaN
    '''

    pass
