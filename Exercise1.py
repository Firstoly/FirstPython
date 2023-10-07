money = float(input('Enter number money withdraw : '))
print ('\n')
B1000 = money // 1000
B500 = (money % 1000)//500
B100 = (money %500)//100
print ('Cash B1000 : ',B1000)
print ('Cash B500 : ',B500)
print ('Cash B100 : ',B100)