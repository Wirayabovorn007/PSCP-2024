'''Cat parade'''
def main():
    '''f'''
    cat = []
    while True:
        x = input()
        if x == 'END':
            break
        if ',' in x and x != 'IT\'S A DOG':
            x = x.split(',')
            for i in x:
                cat.append(i)
        else:
            if x != 'IT\'S A DOG':
                cat.append(x)
        if x == 'IT\'S A DOG':
            cat.pop()
    cat_nd = []
    for i in cat:
        if i[0] == ' ':
            cat_nd.append(i[1:])
        else:
            cat_nd.append(i)
    catnds = cat_nd.copy()
    cat_nd.sort()
    parade = []
    for animal in cat_nd:
        index = catnds.index(animal) + 1
        count = catnds.count(animal)
        meoww = str(animal)+' '+str(index)+' '+str(count)
        if meoww not in parade:
            parade.append(meoww)
    for meow in parade:
        print(meow)
main()
