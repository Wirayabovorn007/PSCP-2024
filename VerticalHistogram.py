'''g'''
def main():
    '''f'''
    txt = input()
    letter = []
    count = []
    for i in txt:
        if i not in letter and i.lower() in 'abcdefghjkilmnopqrstuvwxyz':
            letter.append(i)
    letter.sort()
    for h in letter:
        count.append(txt.count(h))

    for j in range(max(count),0,-1):
        temp_w = ''
        for i in count:
            if i >= j:
                temp_w += '* '
            else:
                temp_w += '  '
        if len(str(j))<2:
            print(' '+str(j)+'  '+temp_w)
        else:
            print(str(j)+'  '+temp_w)
    print('    '+' '.join(letter))
main()
