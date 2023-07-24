def solve(s):
    result = []
    for i in s.split(' '):
        result.append(i.capitalize())
    return ' '.join(result)
