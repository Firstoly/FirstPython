amount = int(input('Enter amount : '))
rate = float(input('Enter rate : '))/100
year = int(input('Enter year : '))
value = amount*(1+rate)**year
print ('Future value = ',value)