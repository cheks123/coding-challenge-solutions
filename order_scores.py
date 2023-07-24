def special_sort(scores):
    
    length = len(scores)

    i = 0
    while i < length:
        j = 0
        while j < length - i - 1:
            if scores[j][1] > scores[j+1][1]:
                temp = scores[j + 1]
                scores[j + 1] = scores[j]
                scores[j] = temp
            j += 1
        i += 1
    print(scores)


    scores2 = [[i[0], int(str(i[1])[0]) + int(str(i[1])[1])] for i in scores]
    print(scores2)

    length = len(scores2)
    i = 0
    while i < length:
        j = 0
        while j < length - i - 1:
            if scores2[j][1] > scores2[j+1][1]:
                temp = scores2[j + 1]
                scores2[j + 1] = scores2[j]
                scores2[j] = temp
            j += 1
        i += 1
    print(scores2)
        
    i = 0
    while i < length:
        j = 0
        while j < length - i - 1:
            if (scores2[j][1] == scores2[j + 1][1]) and (scores2[j][0] > scores2[j + 1][0]):
                temp = scores2[j + 1]
                scores2[j + 1] = scores2[j]
                scores2[j] = temp
            j += 1
        i += 1
    print(scores2)
            
    
if __name__ == '__main__':
    scores = [('Anthony', 45), ('Benny', 62), ('Carson', 98),
          ('Donald', 88), ('Elvis', 54), ('Fedrich', 70),
          ('George', 92), ('Henry', 68), ('Ivy', 79), ('Jerry', 81)]
    special_sort(scores)
