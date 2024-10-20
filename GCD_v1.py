'''f'''
def main():
    '''f'''
    lst = []
    num1 = int(input())
    num2 = int(input())
    n = 0
    if num1>num2:
        n = num1
    else:
        n = num2
    for i in range(1,n+1):
        if not num1%i and not num2%i:
            lst.append(i)
    print(max(lst))
main()
