import json

with open('angola_adm2.geojson', 'r') as f:
    data = json.load(f)

names = sorted([f['properties']['shapeName'] for f in data['features']])
for name in names:
    print(name)
