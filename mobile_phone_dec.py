def wrapper(f):
    def fun(l):
        f('+91 '+c[-10:-5]+' '+c[-5:] for c in l)
        # complete the function
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
