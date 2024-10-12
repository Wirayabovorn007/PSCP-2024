'''d'''
def main():
    '''d'''
    code = input()
    num = ''
    sum_num = 0
    for i in code:
        if i.isnumeric():
            num+=i
        else:
            num+=' '
    num = num.split()
    for j in num:
        sum_num+=int(j)
    print(sum_num)
main()
