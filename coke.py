'''d'''
def findlowestvalue(num1,num2):
    '''m'''
    if num1<num2:
        return num1
    return num2

def cost(a1, b1, c1, d1):
    '''f'''
    total_cost = 0
    bottles_bought = 0  #ขวดที่ซื้อมาแล้ว
    caps = 0  #ฝาที่มี
    if b1>0:
        while bottles_bought < d1:
            #ต้องซื้อกี่ขวดถึงจะครบที่ต้องการ
            remaining_bottles = d1 - bottles_bought
            if caps >= b1:
                exchange_bottles = caps // b1
                exchange_bottles = findlowestvalue(exchange_bottles, remaining_bottles)
                total_cost += exchange_bottles * c1
                bottles_bought += exchange_bottles
                caps = caps - exchange_bottles * b1 + exchange_bottles
            else:
                buy_bottles = findlowestvalue(remaining_bottles, (b1 - caps))
                total_cost += buy_bottles * a1
                bottles_bought += buy_bottles
                caps += buy_bottles
    else:
        total_cost += a1*d1
    return total_cost

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(cost(a, b, c, d))
