'''g'''
def main(k,n):
    '''f'''
    candidate = {}
    for i in range(1,k+1):
        candidate[i] = 0
    for _ in range(1,n+1):
        x = int(input())
        if x in candidate:
            candidate[x]+=1
    sum_s = sum(candidate.values())
    sc = []
    for candi,score in candidate.items():
        sc.append(score)
        if score > sum_s/2:
            return candi,score
    return 0, max(sc)


a = int(input()) #จน.ลงสมัคร
b = int(input()) #จน.ลงคะแนน
print(*main(a,b))
