from collections import OrderedDict

words = OrderedDict()

for _ in range(int(input())):
    word = input()
    words[word] = words.get(word, 0) + 1

print(len(words))
print(' '.join(list(map(str, list(words.values())))))

'''
>>>input
4
bcdef
abcdefg
bcde
bcdef

>>>output
3
2 1 1
'''
