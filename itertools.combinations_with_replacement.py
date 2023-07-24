from itertools import combinations_with_replacement as cwr
print(*sorted([''.join(j) for j in [sorted(i) for i in list(cwr('HACK', 2))]]), sep='\n')
