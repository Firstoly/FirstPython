number = int(input('Enter number12 (1-15) : '))
if (number < 1) or (number > 15):
    print ('Enter new number')
else:
    num1 = number % 2
    num1x = number //2
    num2 = num1x % 2
    num2x = num1x //2
    num3 = num2x % 2
    num3x = num2x // 2
    num4 = num3x %2
    num4x = num3x //2
sum = (f'{num4}{num3}{num2}{num1}')
print ('number two : ',sum)