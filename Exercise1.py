print('>> Program Find Maximum Digit <<')
loop = True
while loop:
    number = str(input('Enter integer number (0-exit) : '))
    if number == '0':
        print('Exit Program....') 
        break
    else:
        Max = max(number)
        print ('Maximum Sigit if integer number ',number,'=',Max)