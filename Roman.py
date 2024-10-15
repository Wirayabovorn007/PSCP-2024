'''c'''
roman = input()
ARABIC = 0
if 'IV' in roman:
    ARABIC += 4
    roman = roman.replace('IV', '')
if 'IX' in roman:
    ARABIC += 9
    roman = roman.replace('IX', '')
if 'CM' in roman:
    ARABIC += 900
    roman = roman.replace('CM', '')
if 'CD' in roman:
    ARABIC += 400
    roman = roman.replace('CD', '')
if 'XC' in roman:
    ARABIC += 90
    roman = roman.replace('XC', '')
if 'XL' in roman:
    ARABIC += 40
    roman = roman.replace('XL', '')
if 'I' in roman:
    ARABIC += 1 * roman.count('I')
    roman = roman.replace('I', '')
if 'V' in roman:
    ARABIC += 5 * roman.count('V')
    roman = roman.replace('V', '')
if 'X' in roman:
    ARABIC += 10 * roman.count('X')
    roman = roman.replace('X', '')
if 'L' in roman:
    ARABIC += 50 * roman.count('L')
    roman = roman.replace('L', '')
if 'C' in roman:
    ARABIC += 100 * roman.count('C')
    roman = roman.replace('C', '')
if 'D' in roman:
    ARABIC += 500 * roman.count('D')
    roman = roman.replace('D', '')
if 'M' in roman:
    ARABIC += 1000 * roman.count('M')
    roman = roman.replace('M', '')
print(ARABIC)
