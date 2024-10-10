'''g'''
def main():
    """CcC"""
    input_text = input().replace(".", "")
    words = input_text.split()
    result_list = []

    for word in words:
        vowel_count = sum(1 for letter in word.lower() if letter in "aeiou")
        if vowel_count >= 2:
            result_list.append(word)

    result_list.sort()

    if result_list:
        for word in result_list:
            print(word)
    else:
        print("Nope")
main()
