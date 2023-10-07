print ('>> Program Check Palindrome <<')
number = int(input('Enter integer number (4 digit) : '))
if (number < 1000) or (number > 9999):
    print ('Enter integer number \"4 Digit\" only!')
else:
    n1 = number % 10
    n1x = number //10
    n2 = n1x % 10
    n2x = n1x //10
    n3 = n2x % 10
    n3x = n2x //10
    n4 = n3x % 10
    n4x = n3x //10
if (n1==n4)and(n2==n3):
    print ('Your number is ',number,',is palindrome')
elif (n1!=n4)and(n2!=n3):
    print ('Your number is ',number,',is not palindrome')

    

    