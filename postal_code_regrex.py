import re

p1 = '121426'
p2 = '523563'
p3 = '552523'
p4 = '110000'

pattern = r'^[1-9]([0-9]{5})$'
pattern2 = r'(?=(\d)\d\1)'

result = re.findall(pattern2, p2)
print(result)
