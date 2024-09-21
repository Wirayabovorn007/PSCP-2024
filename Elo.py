'''f'''
def main():
    '''h'''
    ra = float(input())
    rb = float(input())
    o = input()
    ea = 1 / (1+10**((rb - ra)/400))
    eb = 1 / (1+10**((ra - rb)/400))
    if o == 'A':
        print(f'{ea:.2f}')
    else:
        print(f'{eb:.2f}')
main()
