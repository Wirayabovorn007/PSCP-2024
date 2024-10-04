'''d'''
def main():
    '''d'''
    origin = input()
    change = input()
    diff = ''
    for i,j in enumerate(change):
        if j != origin[i]:
            diff+=j
    print(len(diff))
main()
