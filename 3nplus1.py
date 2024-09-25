'''f'''
def cal(n):
    '''f'''
    count = 1
    while True:
        if n <=1:
            break
        if not n%2:
            n = n/2
            count += 1
        elif n%2:
            n = (n*3)+1
            count += 1
    return count
def main():
    '''d'''
    lst_num = []
    while True:
        n = int(input())
        if not n:
            break
        lst_num.append(cal(n))
    for i in lst_num:
        print(i)
main()
