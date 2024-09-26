'''p'''
from math import log2
def main():
    '''f'''
    pw = input()
    l = len(pw)
    case1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    case2 = 'abcdefghijklmnopqrstuvwxyz'
    case3 = '0123456789'
    case4 = '~`!@#$%^&*()-_+=[]{\\}|/:;"\'<>,.?'
    r = 0
    if any(char in case1 for char in pw):
        r += 26  # Upper
    if any(char in case2 for char in pw):
        r += 26  # Lower
    if any(char in case3 for char in pw):
        r += 10  # Num
    if any(char in case4 for char in pw):
        r += len(case4)

    if r > 0:
        e = log2(r**l)
        print(int(e))
        if int(e) < 28:
            print('Very Weak')
        elif 28 <= int(e) <= 35:
            print('Weak')
        elif 36 <= int(e) <= 59:
            print('Reasonable')
        elif 60 <= int(e) <= 127:
            print('Strong')
        else:
            print('Very Strong')
main()
