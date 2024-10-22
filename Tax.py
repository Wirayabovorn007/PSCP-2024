'''f'''
def main():
    '''g'''
    year = int(input())
    cc = int(input())
    total = 0
    if cc >= 1:
        if cc <= 600:
            total += cc * 0.5
        else:
            total += 600 * 0.5
    if cc > 600:
        if cc <= 1800:
            total += (cc - 600) * 1.5
        else:
            total += 1200 * 1.5
    if cc > 1800:
        total += (cc - 1800) * 4
    if year == 6:
        total -= total * 0.10
    elif year == 7:
        total -= total * 0.20
    elif year == 8:
        total -= total * 0.30
    elif year == 9:
        total -= total * 0.40
    elif year >= 10:
        total -= total * 0.50
    print(f'{total:.2f}')
main()
