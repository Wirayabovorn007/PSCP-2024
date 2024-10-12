'''d'''
def check(a):
    '''d'''
    b = 0
    if 100<=a<=150:
        b+=5000
    elif 151<=a<=250:
        b+=6000
    elif 251 <=a<=300:
        b+=7000
    elif 301<=a<=350:
        b+=8000
    elif 351<=a<=400:
        b+=9000
    elif 401<=a<=450:
        b+=10000
    elif 451<=a<=550:
        b+=12000
    elif 551<=a<=700:
        b+=14000
    elif 701<=a<=1000:
        b+=18000
    elif 1001<=a<=1200:
        b+=21000
    elif 1201<=a<=1400:
        b+=23000
    elif 1401<=a<=1500:
        b+=24000
    elif 1501<=a<=2000:
        b+=30000
    elif 2001<=a<=2500:
        b+=34000
    return b

def main():
    '''d'''
    area = int(input())
    height = int(input())
    people = int(input())
    status = input()  
    sun_light = input()
    btu = 0
    if 100<=area<=2500:
        btu+=check(area)
        if height-8>0:
            btu+=(height-8)*1000
        if people-2>0:
            btu+=(people-2)*600
        if status == 'kitchen':
            btu+=4000
        if sun_light == 'facing the sun':
            btu+=btu*(10/100)
        if sun_light == 'shaded':
            btu-=btu*(10/100)
    print(int(btu))
main()
