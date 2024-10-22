'''f'''
from math import gcd
def main():
    '''f'''
    num1 = int(input())
    num2 = int(input())
    if gcd(num1, num2) == 1:
        print('YES')
        print(gcd(num1, num2))
    else:
        print('NO')
        print(gcd(num1, num2))
main()
