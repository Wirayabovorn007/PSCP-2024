'''f'''
def main():
    '''d'''
    word = input()
    letter = []
    count = []
    word = word.lower()
    for i in word:
        if i not in letter and i != ' ':
            letter.append(i)
            count.append(word.count(i))
    for j in letter:
        if word.count(j) == max(count):
            print(j)
main()
