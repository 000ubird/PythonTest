'''
Created on 2018/08/27

@author: User
'''

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

if __name__ == '__main__':
    #サンプルデータ
    #https://en.wikipedia.org/wiki/List_of_all-time_NFL_win%E2%80%93loss_records
    nfl_frame = pd.read_clipboard()
    print(nfl_frame)
    '''
        Rank                     Team    ...     First NFL Season   Division
    0      1           Dallas Cowboys    ...                 1960   NFC East
    1      2        Green Bay Packers    ...                 1921  NFC North
    2      3            Chicago Bears    ...                 1920  NFC North
        ～～～～
    29    30           Houston Texans    ...                 2002  AFC South
    30    31        Arizona Cardinals    ...                 1920   NFC West
    31    32     Tampa Bay Buccaneers    ...                 1976  NFC South
    '''

    #列名を出力する
    print(nfl_frame.columns)    #Index(['Rank', 'Team', 'GP', 'Won', 'Lost', 'Tied', 'Pct.', 'First NFL Season', 'Division'], dtype='object')

    #指定の列のみを出力
    print(nfl_frame['First NFL Season'])
    '''
    0     1960
    1     1921
    2     1920
            ～～～
    30    1920
    31    1976
    Name: First NFL Season, dtype: int64
    '''

    #一単語であれば、属性にアクセスするような形で参照可能
    print(nfl_frame.Team)
    '''
    0              Dallas Cowboys
    1           Green Bay Packers
    2               Chicago Bears
                ～～～
    30          Arizona Cardinals
    31       Tampa Bay Buccaneers
    Name: Team, dtype: object
    '''

    #複数の列にアクセス
    print(nfl_frame[ ['First NFL Season', 'Team'] ])

    #新しいデータフレームを作る
    DataFrame(nfl_frame, columns=['First NFL Season', 'Team'])

    #存在しない列を指定してデータフレームを作ることも可能
    #その場合、値はnullになる
    DataFrame(nfl_frame, columns=['First NFL Season', 'Team', 'null_column'])
    nfl_frame['null_column'] = "this is test!"  #これで全体に代入可能
    nfl_frame['null_column'] = np.arange(32)    #こんなふうにもいける

    print(nfl_frame.head()) #先頭の5行を出力
    print(nfl_frame.tail()) #末尾の5行を出力

    #指定の行へアクセスする
    print(nfl_frame.ix[2])
    '''
    Rank                            3
    Team                Chicago Bears
    GP                          1,370
    Won                           749
    Lost                          579
    Tied                           42
    Pct.                        0.562
    First NFL Season             1920
    Division                NFC North
    Name: 2, dtype: object
    '''

    #インデックスを指定して、値の代入が可能
    teams = Series(["hogehoge", "fugafuga"], index=[4,0])
    nfl_frame['Team'] = teams
    print(nfl_frame)

    #列の削除
    del nfl_frame['Team']
    print(nfl_frame)

    #Pythonの辞書型からデータフレームを生成できる
    data_dict = {'key':['aaa', 'bbb', 'ccc'], 'value':[100,200,300]}
    print(data_dict)    #{'key': ['aaa', 'bbb', 'ccc'], 'value': [100, 200, 300]}

    dict_frame = DataFrame(data_dict)
    print(dict_frame)
    '''
        key  value
    0  aaa    100
    1  bbb    200
    2  ccc    300
    '''

    pass
