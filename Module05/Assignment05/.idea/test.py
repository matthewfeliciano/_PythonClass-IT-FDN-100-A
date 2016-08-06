item1 = { "item": "mouse", "value": 23.0 }
print(item1)
print(item1["value"])
item1["status"] = "high"
print(item1)
print(item1["value"])
#  OUTPUT:
{'item': 'mouse', 'value': 23.0}
23.0
{'item': 'mouse', 'value': 23.0, 'status': 'high'}
23.0
