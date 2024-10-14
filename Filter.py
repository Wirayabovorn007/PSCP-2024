'''d'''
def main():
    '''d'''
    data = input()
    fl_value = float(input())
    lst = ''
    for i in data:
        if i not in ('{','}','"',':'):
            lst+=i
    x = lst.split(',')
    filtered = []
    for j in x:
        if float(j[9:])>=fl_value:
            filtered.append(j[:9].strip()+'\t'+j[9:].strip())
    filtered = sorted(filtered, key=lambda x: x[:9])
    for u in filtered:
        if '.' in u[-2:]:
            u+='0'
        print(u)
    if not filtered:
        print('Nope')
main()
