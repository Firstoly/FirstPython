from os import system
from random import randint
from time import sleep


def main():
    product = ["Cocoa", "Foi Thong", "Thai tea",
               "Green tea", "Strawberry", "Mango"]
    price = [75.0, 85.0, 95.0, 105.0]
    stock = []
    stockDefault = []
    numberOrder = 0
    OrderList = []

    RandomStock(product, stock, stockDefault)

    mainMenu = True
    while (mainMenu):
        system('cls')

        print('====== BINGSU ======\n')
        print('1) Sell Product')
        print('2) Warehouse')
        print('3) Report')
        print('0) Exit Program')
        print('\n'+('-'*20)+'\n')

        inputMenu = input('Choose menu : ')
        if (inputMenu == '1'):
            Sell(product, price, stock, stockDefault, numberOrder, OrderList)
        elif (inputMenu == '2'):
            system('cls')
            Warehouse(product, price, stock, stockDefault)
            system('pause')
        elif (inputMenu == '3'):
            ReportOrder(OrderList)
        elif (inputMenu == '0'):
            print('\nExit ',end='')
            for i in range(3):
                sleep(0.5)
                print('.',end='')
            
            sleep(1)
            print()    
            mainMenu = False
        else:
            print('\nInvalid menu, try again.')
            sleep(1.5)


def Sell(product, price, stock, stockDefault, numberOrder, OrderList):
    chooseMenu = False;
    chooseSize = False
    enterAmount = False
    confirm = False
    success = False
    amountItem = 0
    cartItem = []

    
    while (not success):
        while (not chooseMenu):
            system('cls')
            Warehouse(product, price, stock, stockDefault)
            cartItem.append(['', '', 0.0, 0])

            print('(Y=Confirm, X=Cancel, T=Cart)')
            menu = input('Enter menu No. : ')
            menu = menu.upper()

            if (menu >= '1' and menu <= '6'):
                menu = int(menu)-1
                chooseMenu = True
            elif (menu == 'Y'):
                chooseMenu = True
                success = True
                confirm = True
            elif (menu == 'X'):
                chooseMenu = True
                success = True
            elif (menu == 'T'):
                system('cls')
                Cart(amountItem, cartItem, success)
            else:
                print('\nInvalid menu No., try again.')
                sleep(2)

        while (not chooseSize and not success):
            system('cls')

            line = ('-'*20)
            size = ['S', 'M', 'L', 'XL']
            IDsize = ['A)', 'B)', 'C)', 'D)']

            print('Bingsu Size\n')
            print(line)
            print('ID   Size     Price')
            print(line)
            for i in range(len(size)):
                print(f'%2s    %-6s%7.2f' % (IDsize[i], size[i], price[i]))
            print(line, end='\n\n')
            enterSize = input('Enter Size ID : ')
            enterSize = enterSize.lower()

            if (enterSize >= 'a' and enterSize <= 'd'): 
                chooseSize = True

                while (not enterAmount):
                    system('cls')
                    print('Bingsu Size\n')
                    print(line)
                    print('ID   Size     Price')
                    print(line)
                    for i in range(len(size)):
                        print(f'%2s    %-6s%7.2f' % (IDsize[i], size[i], price[i]))
                    print(line, end='\n\n')
                    print(f'Enter Size ID : {enterSize.upper()}')
                    enterSize = ord(enterSize)-97

                    amount = input('Enter amount : ')
                    if (amount.isdigit()):
                        if (int(amount)<=0):
                            print('\nIncorrect quantity, try again.')
                            sleep(1.5)
                        else:
                            enterAmount = True

                            if (int(amount)>stock[menu]):
                                amount = stock[menu]
                                stock[menu] = 0
                            else:
                                stock[menu] = stock[menu]-int(amount)

                            cartDuplicate = False
                            for i in range(amountItem):
                                if (menu==cartItem[amountItem][0]):
                                    cartItem[amountItem][2] += int(amount)
                                    cartDuplicate = True
                                    break
                            if (not cartDuplicate):
                                cartItem[amountItem][0] = product[menu]
                                cartItem[amountItem][1] = size[enterSize]
                                cartItem[amountItem][2] = price[enterSize]
                                cartItem[amountItem][3] = int(amount)
                                amountItem += 1
                    else:
                        print('\nIncorrect quantity, try again.')
                        sleep(1.5)
            else:
                print('\nInvalid size ID, try again.')
                sleep(2)

        chooseMenu = False
        chooseSize = False
        enterAmount = False

    
    if (success):
        totalOrder = 0.0
        line = ('-'*39)

        system('cls')
        if (confirm):
            numberOrder += 1
            print(f'Order #{numberOrder} :Confirm')
            Cart(amountItem, cartItem, success)
            OrderList.append(cartItem)
        else:
            print('Cancel\n')
            Cart(amountItem, cartItem, success)
        


def Cart(amountItem, cartItem, success):
    line = ('-'*39)
    totalCart = 0.0
    
    if (not success):
        print('Product in the cart\n')
    print(line)
    print('Product      Size       Price      Qty.')
    print(line)

    for i in range(amountItem):
        print(f'%-13s%3s%13.2f%9d' %(cartItem[i][0], cartItem[i][1], cartItem[i][2], cartItem[i][3]))
        totalCart += cartItem[i][2]*cartItem[i][3]

    print('\n'+f'Total price :  $%.2f'.rjust(42-len(str(totalCart))) %(totalCart))
    print(line, end='\n\n')
    system('pause')



def Warehouse(product, price, stock, stockDefault):
    line = ('-'*25)

    print('Bingsu Menu\n')
    print(line)
    print('No.  Product        Stock')
    print(line)
    for i in range(len(product)):
        print(f'{i+1}'.rjust(2)+'   ' +product[i].ljust(13)+f'%6d' % (stock[i]))
    print(line, end='\n\n')



def RandomStock(product, stock, stockDefault):
    for i in range(len(product)):
        stock.append(randint(5, 25))
        stockDefault.append(stock[i])



def ReportOrder(OrderList):
    line = ('-'*47)
    lineEq = ('='*47)
    
    system('cls')
    print('Report Order\n')
    print(lineEq)
    print('Order   Product      Size       Price      Qty.')
    print(lineEq)
    
    for i in range(len(OrderList)):
        Total = 0.0

        print(f' #%02d'.rjust(4) %(i+1)+(' '*4), end='')
        for k in range(len(OrderList[i])-1):
            if (k>0):
                print(' '*8, end='')
            print(f'%-13s%3s%13.2f%9d' %(OrderList[i][k][0], OrderList[i][k][1], OrderList[i][k][2], OrderList[i][k][3]))
            Total += OrderList[i][k][2]*OrderList[i][k][3]
        print('\n'+f'Total price :  $%.2f\n'.rjust(47) %(Total))
        print(line)
    print()
    system('pause')



main()
