volt = float (input('Enter the voltage value (E) of the power supply(Volts) : '))
r1 = float(input('Enter the first resistance 1 (R1: Ohm) : '))
r2 = float(input('Enter the first resistance 2 (R2: Ohm) : '))
r3 = float(input('Enter the first resistance 3 (R3: Ohm) : '))
sum = r1+r2+r3
amp = volt / sum
r1 *= amp
r2 *= amp
r3 *= amp
print ('Current value (I) of the circuit : ',amp,'volt')
print('Value of voltage drop across resistance number 1 :','%.2f' % r1,'ohm')
print('Value of voltage drop across resistance number 2 :','%.2f' % r2,'ohm')
print('Value of voltage drop across resistance number 3 :','%.2f' % r3,'ohm')