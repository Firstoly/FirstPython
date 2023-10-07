loop = True
n = 0
text = ''
sum = 0
while loop:
    print()
    print(22*'=')
    print('|     Drinks Menu    |')
    print(22*'=')
    print('| 0. Quit             |')
    print('| 1. Hot Coffee       |')
    print('| 2. Ice Coffee       |')
    print('| 3. Frappe Cofee     |')
    print('| 4. Calculate Cost   |')
    print(22*'=')
    Item = int(input('Select Item : '))
    if (Item == 0)or(Item > 4):
        print('Exit Program ...')
        break
    elif Item == 1:
        glasses = int(input('Hot Coffee, how many glasses : '))
        many = 35
        many1 = '%.2f'%many
        name = 'Hot Coffee'
        Total = many * glasses
        Total1 = '%.2f'%Total 
        sum += float(Total1)
        text += (f'{glasses}'.ljust(5) + f'{name}'.ljust(17) + f'{many1}'.rjust(3)+f'{Total1}'.rjust(9) +'\n')  

    elif Item == 2:
        glasses = int(input('Ice Coffee, how many glasses : '))
        many = 50
        many1 = '%.2f'%many
        name = 'Ice Coffee'
        Total = many * glasses
        Total1 = '%.2f'%Total 
        sum += float(Total1)
        text += (f'{glasses}'.ljust(5) + f'{name}'.ljust(17) + f'{many1}'.rjust(3)+f'{Total1}'.rjust(9) +'\n')  

    elif Item == 3:
        glasses = int(input('Frappe Coffee, how many glasses : '))
        many = 60
        many1 = '%.2f'%many
        name = 'Frappe Coffee'
        Total = many * glasses
        Total1 = '%.2f'%Total 
        sum += float(Total1)
        text += (f'{glasses}'.ljust(5) + f'{name}'.ljust(17) + f'{many1}'.rjust(3)+f'{Total1}'.rjust(9) +'\n')      
    else:
        n += 1
        print()
        print ('Order #',n,':')
        print (40*'-')
        print ('Qty  Item'.ljust(15)+'price   Total'.rjust(20))
        print (40*'-')
        print (text)
        print (40*'-')
        print ('Total : ','%.2f'%sum,'Bath')



        
