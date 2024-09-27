'''f'''
def  main():
    '''f'''
    age = int(input())
    weight = float(input())
    count = int(input())
    if age == 17 or 60<=age<=70:
        certifi = input()
        if not count:
            if weight>=45 and age<=55 and certifi == 'True':
                print('Yes')
            else:
                print('No')
        else:
            if weight>=45 and certifi == 'True':
                print('Yes')
            else:
                print('No')
    else:
        if not count:
            if 17<=age<=55 and weight>=45:
                print('Yes')
            else:
                print('No')
        else:
            if 17<=age<=70 and weight>=45:
                print('Yes')
            else:
                print('No')
main()
