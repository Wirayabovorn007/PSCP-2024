'''d'''
def main():
    '''d'''
    text = input()
    lower_t = []
    upper_t = []
    counted = ''
    for i in text:
        frequency = ''
        c = 0
        if i.isupper() and i not in counted:
            for _ in range(1,text.count(i)+1):
                if c == 5:
                    c = 0
                    frequency +='|'
                frequency += '-'
                c+=1
            upper_t.append(i+' : '+frequency)
            counted+=i
        if i.islower() and i not in counted:
            for _ in range(1,text.count(i)+1):
                if c == 5:
                    c = 0
                    frequency +='|'
                frequency += '-'
                c+=1
            lower_t.append(i+' : '+frequency)
            counted+=i
    lower_t.sort()
    upper_t.sort()
    lower_t.extend(upper_t)
    for ans in lower_t:
        print(ans)
main()
