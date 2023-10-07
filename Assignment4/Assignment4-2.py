loop = True
text = ''
totalpoin = 0
TotalCredits = 0
print (60*'=')
print ('\t| Program Calculate Grade Point Average |')
print (60*'=')
print ('Input Data:')
while loop:
    for i in range (1,6):
        name = str(input(f'Enter subject name {(i)} : '))
        score = float(input(f'Enter subject score {(i)} : '))
        if score > 79:
            gra = 'A'
            point = 4.0
        elif score > 69:
            gra = 'B'
            point = 3.0
        elif score > 59:
            gra = 'C'
            point = 2.0
        elif score > 49:
            gra = 'D'
            point = 1.0
        elif score <= 49 :
            gra = 'F'
            point = 0.0
        print ()
        text += (f'{i}'.rjust(3) + f'{name}'.rjust(5) + f'{score}'.rjust(23) + f'{gra}'.rjust(7) + f'{point}'.rjust(11)+'\n')
        totalpoin += point*3
        TotalCredits = 5*3.0
        sum = totalpoin/TotalCredits
    loop = False
print (f'Grade Poin Average (GPA) Report'.center(51))
print (51*'=')
print (f'NO.'.rjust(4) + f'Subject Name'.rjust(13) + f'Mark'.rjust(14) + f'Grade'.rjust(9) + f'Points'.rjust(11))
print (51*'=')
print (text)
print (51*'=')
print ('Total Poins : ',totalpoin)
print ('Total Credits : ',TotalCredits)
print ('Grade Poin Average (GPA) : ','%.2f'%sum)
