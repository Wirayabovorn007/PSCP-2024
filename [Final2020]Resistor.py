'''d'''
def check_one_two(n):
    '''d'''
    l = ''
    if n == 'Black':
        l ='0'
    elif n == 'Brown':
        l = '1'
    elif n == 'Red':
        l = '2'
    elif n == 'Orange':
        l = '3'
    elif n == 'Yellow':
        l = '4'
    elif n == 'Green':
        l = '5'
    elif n == 'Blue':
        l = '6'
    elif n == 'Purple':
        l = '7'
    elif n == 'Grey':
        l = '8'
    elif n == 'White':
        l = '9'
    if l:
        return l
    return 'Error'

def check_three(t):
    '''d'''
    k = 0
    if t == 'Black':
        k = 1
    elif t == 'Brown':
        k = 10
    elif t == 'Red':
        k = 100
    elif t == 'Orange':
        k = 1000
    elif t == 'Yellow':
        k = 10000
    elif t == 'Green':
        k = 100000
    elif t == 'Blue':
        k = 1000000
    elif t == 'Purple':
        k = 10000000
    elif t == 'Gold':
        k = 0.1
    elif t == 'Silver':
        k = 0.01
    if k:
        return k
    return 0

def check_four(p):
    '''f'''
    j = 0
    if p == 'Brown':
        j = 1
    elif p == 'Red':
        j = 2
    elif p == 'Green':
        j = 0.5
    elif p == 'Blue':
        j = 0.25
    elif p == 'Purple':
        j = 0.1
    elif p == 'Grey':
        j = 0.05
    elif p == 'Gold':
        j = 5
    elif p == 'Silver':
        j = 10
    if j :
        return j
    return 0

def resistor():
    '''d'''
    one = input()
    two = input()
    three = input()
    four = input()
    one = check_one_two(one)
    two = check_one_two(two)
    multiply = check_three(three)
    four = check_four(four)
    if 'Error' not in (one+two) and multiply and four:
        lower = (int(one+two)*multiply) - ((int(one+two)*multiply)*(four/100))
        upper = (int(one+two)*multiply) + ((int(one+two)*multiply)*(four/100))
        print(f'{lower:.4f}')
        print(f'{upper:.4f}')
    else:
        print('Error')
resistor()
