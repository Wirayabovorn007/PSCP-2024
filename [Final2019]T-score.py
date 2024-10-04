'''T-score'''
from math import sqrt
def main():
    '''Calculate T-Score'''
    n = int(input())
    _ = int(input())
    x_sum = 0
    x_sum_squared = 0
    score_da = []
    for _ in range(n):
        score = int(input())
        x_sum += score
        x_sum_squared += score**2
        score_da.append(score)
    x_bar = x_sum / n
    if n > 1:
        sd = sqrt((n * x_sum_squared - x_sum**2) / (n * (n - 1)))
    else:
        sd = 0
    for score in score_da:
        if not sd:
            z = 0
        else:
            z = (score - x_bar) / sd
        t_score = 50 + 10 * z
        print(f'{t_score:.2f}')
main()
