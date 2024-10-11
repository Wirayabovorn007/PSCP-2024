'''f'''
def main():
    '''f'''
    money = int(input())
    while True:
        x = input()
        if x == 'END':
            break
        if x[0] == 'D':
            money+=int(x[2:])
        if x[0] == 'W':
            money-=int(x[2:])
        if money<0:
            money = 0
    print(money)
main()
