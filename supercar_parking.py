'''f'''
def main():
    '''f'''
    park_lot = input()
    count = 0
    i = 0
    while i < len(park_lot):
        if park_lot[i] == '0' and (not i or park_lot[i-1] == '0') \
            and (i == len(park_lot)-1 or park_lot[i+1] == '0'):
            count+=1
            i+=2
        else:
            i+=1
    print(count)
main()
