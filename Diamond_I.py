'''j'''
def diamond():
    '''f'''
    ls = []
    m = int(input())
    n = int(input())
    x = input()
    x = x.split()
    if m == 1:
        for g in x:
            ls.append(int(g))
    else:
        ls.extend(x)
        for _ in range(m-1):
            x = input()
            x = x.split()
            for i in range(n):
                ls[i] = int(ls[i])
                ls[i] += int(x[i])
    print(max(ls))
diamond()
