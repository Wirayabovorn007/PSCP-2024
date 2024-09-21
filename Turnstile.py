'''fx'''
def main():
    '''f'''
    count = 0
    state = False #locked
    while True:
        n = input()
        if n == "END":
            break
        if n == "C":
            state = True
        if state is True and n == "P":
            count+=1
            state = False
    print(count)
main()
