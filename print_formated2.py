def print_formatted(number):
    result = [[str(i + 1), str(oct(i+1))[2:], str(hex(i+1))[2:].upper(), str(bin(i+1))[2:]] for i in range(number)]
    
    w = len(str(result[-1][-1]))
    for i in result:
        print(i[0].rjust(w, ' '), i[1].rjust(w, ' '), i[2].upper().rjust(w, ' '), i[3].rjust(w, ' '))


print_formatted(17)
        
