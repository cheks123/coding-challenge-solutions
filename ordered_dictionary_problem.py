from collections import OrderedDict

n = int(input())

items = OrderedDict()
for _ in range(n):
    record = input().split(' ')
    item_name = ' '.join(record[:-1])
    price = record[-1]
    items[item_name] = items.get(item_name, 0) + int(price)

for i, p in items.items():
    print(i, p)

'''
input>>
10
Rice 80
Beans 70
Garri 90
Beans 30
Garri 80
Rice 85
Rice 72
Beans 91
Meat 68

output>>
Beans 43
Rice 237
Beans 234
Garri 170
Meat 68
,,,
