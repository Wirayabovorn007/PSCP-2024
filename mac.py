'''m'''
def case1(t,b):
    '''check1'''
    n = t.count('-')
    k = t.replace('-','')
    c = 0
    k_state = 0
    for i in k:
        if i in b:
            k_state+=1
    t = t.split('-')
    if k_state == 12:
        for i in t:
            if len(i) == 2:
                c+=1
        if n == 5 and c == 6:
            return True
    return False


def case2(t,b):
    '''check2'''
    n = t.count(':')
    k = t.replace(':','')
    c = 0
    k_state = 0
    for i in k:
        if i in b:
            k_state+=1
    t = t.split(':')
    if k_state == 12:
        for i in t:
            if len(i) == 2:
                c+=1
        if n == 5 and c == 6:
            return True
    return False


def case3(t,b):
    '''ch'''
    n = t.count('.')
    k = t.replace('.','')
    c = 0
    k_state = 0
    for i in k:
        if i in b:
            k_state+=1
    t = t.split('.')
    if k_state == 12:
        for i in t:
            if len(i) == 4:
                c+=1
        if n == 2 and c == 3:
            return True
    return False

def main():
    '''d'''
    t = input()
    base_sib_hok = '0123456789ABCDEFabcdef'
    if case1(t,base_sib_hok):
        print('VALID 1')
    elif case2(t,base_sib_hok):
        print('VALID 2')
    elif case3(t,base_sib_hok):
        print('VALID 3')
    else:
        print('ERROR')
main()
