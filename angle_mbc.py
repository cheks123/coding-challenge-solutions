import math

ab = float(input())
bc = float(input())

ac = math.sqrt(ab ** 2 + bc ** 2)
cm = ac / 2

C = math.asin(ab / ac)
bm = math.sqrt(bc ** 2 + cm ** 2 - 2 * bc * cm * math.cos(C))
tita = math.degrees(math.asin(cm * math.sin(C) / bm))



print(round(tita), '\u00B0', sep='')
