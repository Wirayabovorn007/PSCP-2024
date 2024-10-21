'''f'''
def main():
    '''f'''
    m = int(input())
    n = int(input())
    matrice = ''
    c = 0
    for _ in range(m*n):
        x = input()
        if c == n:
            c = 0
            matrice+='\n'
        matrice+=x+' '
        c+=1
    print(matrice)
main()
