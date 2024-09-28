'''d'''
def count(aa, bb, cc):
    '''d'''
    if aa < cc:
        return 0
    count_result = count(aa / bb, bb, cc)
    total = 1 + bb * count_result
    return total
a = float(input())
b = float(input())
c = float(input())
shot = count(a, b, c)
print(int(shot))
