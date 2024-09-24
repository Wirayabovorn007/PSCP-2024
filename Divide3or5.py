'''f'''
def main():
    '''d'''
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        if not i%3 or not i%5:
            ans+=i
    print(ans)
main()
