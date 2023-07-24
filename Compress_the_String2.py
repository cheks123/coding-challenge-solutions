from itertools import groupby as gb
for key, group in gb(input()):
    print('({}, {})'.format(len(list(group)), key), end=' ')
