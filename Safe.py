'''f'''
def main():
    '''f'''
    letter = ['a','b','c','d','e','f','g','h',\
        'i','j','k','l','m','n','o','p','q','r',\
        's','t','u','v','w','x','y','z']  
    t1 = input().lower()
    t2 = input().lower()
    count = 0
    for i,j in enumerate(t1):
        x = letter.index(t2[i])-letter.index(j)
        if j != t2[i]:
            if x < 0:
                x = x*-1
            if x >13:
                x = 1
                letter.sort(reverse=True)
                for u in letter:
                    if u == t2[i]:
                        break
                    x+=1
            count+=x
    print(count)
main()
