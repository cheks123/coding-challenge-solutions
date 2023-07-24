s = input()
result = []
row = ''
for i in range(len(s)):
    if i == 0:
        row += s[i]
    else:
        if s[i] == s[i - 1]:
            row += s[i]
        else:
            result.append(row)
            row = ''
            row += s[i]
if row != '':
    result.append(row)
print(result)
