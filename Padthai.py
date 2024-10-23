'''f'''
def main():
    '''f'''
    ingredient = ['Pad Thai Sauce','Tofu','Pickle Turnip','Shrimp', \
        'Bean Sprouts','Noodle','Chives','Lime','Egg','Oil','Peanuts']
    taste = ['Sweet','Sour','Salty']

    ingredient.sort()
    taste.sort()

    chef_ingredient = []
    taste_chef = []

    while True:
        x = input()
        if x == 'Cook':
            break
        if x not in chef_ingredient:
            chef_ingredient.append(x)

    chef_ingredient.sort()

    while True:
        y = input()
        if y == 'End':
            break
        if y not in taste_chef:
            taste_chef.append(y)
    taste_chef.sort()
    # ตรวจสอบวัตถุดิบและรสชาติ
    if any(c not in ingredient for c in chef_ingredient):  # วัตถุดิบที่ไม่ถูกต้อง
        print('This is not Pad Thai!!!')
    elif len(chef_ingredient) < len(ingredient):  # วัตถุดิบไม่ครบ
        print('This is bad!')
    elif chef_ingredient == ingredient and (any(v not in taste for\
        v in taste_chef) or len(taste_chef) < len(taste)):  # วัตถุดิบครบแต่รสชาติไม่ครบ
        print('Not Bad...')
    elif chef_ingredient == ingredient and \
        all(v in taste_chef for v in taste):  # วัตถุดิบและรสชาติครบ
        print('Delicious!')
main()
