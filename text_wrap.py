def wrap(string, max_width):
    text = string
    length = len(string)
    n = length // max_width
    width = max_width
    a = 0
    result = []
    for i in range(n):
        a = text[0:width]
        b = text[width+1:]
        result.append(a)
        text = b
    return result

print(wrap('ABCDEFGHIJKMN', 4))
