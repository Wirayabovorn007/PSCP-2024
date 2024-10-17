'''d'''
def impostor():
    '''d'''
    player = {}
    count = 0
    while True:
        x = input()
        if x == 'Start':
            break
        l = ''
        for i in x:
            if i not in ('{','}','"'):
                l+=i
        l = l.split(':')
        player[l[0].strip()] = l[1].strip()
    player = dict(sorted(player.items()))
    died = {}
    while True:
        p = input()
        if p == 'End':
            break
        died[p] = player[p]
        player.pop(p)
    died = dict(sorted(died.items()))
    for ok in player.values():
        if 'Impostor' in ok:
            count += 1
    print(f'{count} Impostor Remains')
    print('***Alive***')
    for k in player:
        print(k+' : '+player[k])
    print('***Dead***')
    for h in died:
        print(h+' : '+died[h])
impostor()
