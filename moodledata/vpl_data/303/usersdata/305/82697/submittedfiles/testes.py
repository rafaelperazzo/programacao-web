# -*- coding: utf-8 -*-
#COMECE A PARTIR DAQUI!
'''
n = int(input('Digite o valor de n: '))
i = 2
contador = 0
while (i < (n-1)):
    if n%i == 0 :
        contador += 1
    i += 1
if contador > 0 :
    print('%d NAO EH primo!' %n)
else:
    print('%d EH PRIMO!' %n)
'''
i = int(input('Digite o valor de i: '))
for i in range (0,101,6):
    print(i)
'''   
i = 1
n = int(input('Digite o valor de n: ')) 
while (n <= 0):
 n = int(input('Digite o valor de n: '))

while (i <= n):
  print(i**2)
  i += 2