# -*- coding: utf-8 -*-
#COMECE A PARTIR DAQUI!
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
    