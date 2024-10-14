'''d'''
def main():
    '''d'''
    original = input()
    change_to = input()
    for i in range(len(original)):
        l = change_to[:i]+original[i:]
        print(l)
    o = 0
    m = ''
    if l != change_to and len(l) < len(change_to):
        for _ in range(len(change_to)-(len(l))):
            if not o:
                x = change_to[:len(l)]
                print(x)
                o+=1
                m+=x
            else:
                if m == change_to:
                    break
                for t in change_to[len(l):]:
                    m+=t
                    print(m)
    else:
        print(change_to)
main()
