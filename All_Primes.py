'''l'''
def is_prime(num):
    '''k'''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            return False
    return True

def main():
    '''v'''
    n = int(input())
    count = 0
    for i in range(2, n+1):
        if is_prime(i):
            count += 1
    print(count)

main()
