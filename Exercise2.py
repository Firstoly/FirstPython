print ('>>Program find MAximum Value <<')
num = int(input('Enter number of value (3-10) :'))
value = True
if (num<3):
    num=3
elif (num>10):
    num=10
Max = 0
value1 = ''
print ('Program get value',num,'numnumbers.')
while value:
        for n in range (1,num+1):
            num1 = int(input(f'Enter value Number #{n}: '))
            if (Max<num1):
                Max=num1
            value1 += str(num1) + ',' 
        break
print ('Your enter number :',value1)
print ('Maximum value number is :',Max)
print ('Exit Program')
