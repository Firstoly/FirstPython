#โปรเเกรมคำนวณการทาสี:
width = float(input('Enter the width of the house (meters) : '))
long = float(input('Enter the long of the house (meters) : '))
high = float(input('Enter the high of the house (meters) : '))
sum = width*long*high
sum2 = '%.2f'% sum
liter = sum / 2.5
can = int(liter / 4)
bath = can * 200
print ()
print ('Total amount of exterior house area to be painted : ',sum2,'meters')
print ('Total number of colors used in painting : ','%.2f'% liter,'liter')
print ('Number of paint cans used for painting : ',can,'can')
print ('Amount spent on paint purchases : ',bath,'baht')
