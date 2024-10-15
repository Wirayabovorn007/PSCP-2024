'''d'''
def main():
    '''d'''
    month = int(input())
    price = 0
    total = 0
    a = float(input()) #a บาท
    b = float(input()) #จำนวนลูกบาศก์
    c = float(input()) #ที่คิดส่วนที่เกินจาก b ลูกบาศก์เมตร
    d = float(input()) #ถ้าเดือนใดใช้น้ำไม่เกินค่า d บาท
    for _ in range(month):
        i = float(input())
        if i >b:
            price=(a*b)+(i-b)*c
        else:
            price = i*a
        if price > d:
            total+=price
    print(f'{total:.2f}')
main()
