'''d'''
def main():
    n =int(input())
    music = {}
    for _ in range(n):
        x = input()
        x = x.split('-')
        if x[0] not in music:
            music[x[0]] = []
            music[x[0]].append(x[1])
        else:
            music[x[0]].append(x[1])

    for key,value in music.items():
        print(f'{key}\n'+'\n'.join(value))
main()
