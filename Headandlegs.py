'''h'''
def main():
    '''d'''
    a = int(input())
    b = int(input())
    if b < 2 * a or b > 4 * a or (b - 2 * a) % 2:
        print('Impossible')
    else:
        x = (b - 2 * a) // 2  #กระต่าย
        y = a - x  #นก
        if x < 0 or y < 0:
            print('Impossible')
        else:
            print(int(x), int(y))
main()
