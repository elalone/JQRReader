import json
from csv import DictWriter

with open('InputData/PCTEExport.json', 'rb') as f:
    data = json.load(f)

rows = []
for item in data['data']:
    rows.append({
        'Name': item['competencyName'],
        'Description': item['competencyDesc'],
        'Status': item['status'],
    })

with open('OutputData/signoffs.csv', 'w', newline='') as f:
    fieldnames = ['Name', 'Description', 'Status']
    writer = DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
