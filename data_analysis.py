import pandas as pd
import json

# CSVファイルの読み込み
df = pd.read_csv('meitetu_sta.csv')

# DataFrameを辞書のリストに変換
data_dict = df.to_dict(orient='records')

# 整形されたJSON文字列を生成
formatted_json = json.dumps(data_dict, ensure_ascii=False, indent=4, separators=(',', ': '))

# JSONファイルとして保存
with open('meitetu_sta.json', 'w', encoding='utf-8') as f:
    f.write(formatted_json)