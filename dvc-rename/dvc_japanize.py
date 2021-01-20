import pandas as pd

df = pd.read_csv('contentlist.txt')

#フォルダーツリーをつくってしまう。

for key, row in df.iterrows():
    print(key)
    print(row)
    print('')

#    print(df['カテゴリーID'])
#    print(df['動画ID'])
#    print(df['製品タイトル'])
#    print(df['カテゴリー'])
#    print(df['コンテンツタイトル'])
#    print(df['コンテンツ概要'])
