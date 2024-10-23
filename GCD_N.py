from math import gcd
from functools import reduce
'''g'''
def main():
    '''f'''
    n = int(input())
    num = []
    for _ in range(n):
        x = int(input())
        num.append(x)
    ans = reduce(gcd, num)
    print(ans)
main()
