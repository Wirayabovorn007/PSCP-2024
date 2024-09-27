'''f'''
def main():
    '''d'''
    t = input()
    invert = ''
    start = 0
    for i in t:
        if i == '1':
            invert+='0'
        if i == '0':
            invert+='1'
    for j in invert:
        if j != '1':
            start+=1
        else:
            break
    print(invert[start:])
main()
