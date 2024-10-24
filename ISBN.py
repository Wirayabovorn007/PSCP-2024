'''f'''
def main():
    '''f'''
    num = input()
    num = num.replace('-','')
    num = num.replace(' ','')
    cal = 0
    j = 0
    for i in range(10,1,-1):
        cal+=(i*int(num[j]))
        j+=1
    cal = -(cal) % 11
    n = 0
    if num[-1] == 'X':
        n = 10
    else:
        n = int(num[-1])

    if n == cal:
        print('Yes')
    else:
        if cal == 10:
            cal = 'X'
        print('No',cal)
main()
