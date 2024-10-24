'''plasom'''
def main():
    '''f'''
    num = input()
    count = 0
    c = 0
    for n,i in enumerate(num):
        c = int(i)
        for j in num[n+1:]:
            c+=int(j)
            if c == 10:
                count += 1
                break
            if c>10:
                break
    print(count)
main()
