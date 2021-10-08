s=input()#Строка
zero=0
one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0
for i in range(0,len(s)):
    if s[i]=='0':
        zero+=1
    if s[i]=='1':
        one+=1
    if s[i]=='2':
        two+=1
    if s[i]=='3':
        three+=1
    if s[i]=='4':
        four+=1
    if s[i]=='5':
        five+=1
    if s[i]=='6':
        six+=1
    if s[i]=='7':
        seven+=1
    if s[i]=='8':
        eight+=1
    if s[i]=='9':
        nine+=1
maxnumber=max(zero,one,two,three,four,five,six,seven,eight,nine)
if maxnumber==zero:
    print('Цифра:',0,'Количество:',maxnumber)
if maxnumber==one:
de    print('Цифра:',1,'Количество:',maxnumber)
if maxnumber==two:
    print('Цифра:',2,'Количество:',maxnumber)
if maxnumber==three:
    print('Цифра:',3,'Количество:',maxnumber)
if maxnumber==four:
    print('Цифра:',4,'Количество:',maxnumber)
if maxnumber==five:
    print('Цифра:',5,'Количество:',maxnumber)
if maxnumber==six:
    print('Цифра:',6,'Количество:',maxnumber)
if maxnumber==seven:
    print('Цифра:',7,'Количество:',maxnumber)
if maxnumber==eight:
    print('Цифра:',8,'Количество:',maxnumber)
if maxnumber==nine:
    print('Цифра:',9,'Количество:',maxnumber)
            
