'''h'''
def main(word):
    '''f'''
    vowels = "aeiouAEIOU"
    for i in range(len(word)-1, -1, -1):
        if word[i] in vowels:
            return word[:i+1] + word[i] * 3 + word[i+1:]
    return word
words = input()
print(main(words))
