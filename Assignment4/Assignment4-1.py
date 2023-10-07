loop = True
while loop:
    number = int(input('Enter number (2-12) : '))
    if (number < 2)or(number > 12):
        print ('Exit')
        break
    else:
        print (50*'-')
        print (f'Multiplication  Table'.center(50))
        print (50*'-')
        for n in range (1,13):
            for row in range (0,4):
                value = (number+row)*n
                base = (number+row)
                print (f'{base}'.rjust(2) + ' * ' + f'{n}'.rjust(2) + ' = ' + f'{value}'.rjust(3) ,end ='|')        
            print()

