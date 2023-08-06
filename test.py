import json
from collections import defaultdict

# JSONデータをロードする
with open('StationsData.json', 'r') as f:
    data = json.load(f)['StationsData']

# IDをキーとした辞書を作成する。そのキーに対応する値は、そのIDを持つ駅のリストである。
stations_by_id = defaultdict(list)
for station in data:
    stations_by_id[station['id']].append(station)

# 同じIDを持つ駅を探し、その情報を表示する
for station_id, stations in stations_by_id.items():
    if len(stations) > 1:
        print(f'Duplicate stations with id {station_id}:')
        for station in stations:
            print(json.dumps(station, indent=2))
