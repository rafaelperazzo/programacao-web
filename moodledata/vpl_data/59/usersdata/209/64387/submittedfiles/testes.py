# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def vampiro(x):
    z=x//100
    a=(z//10)+(z%10)*10
    b=x%100
    if a*b==x:
        return True
    else:
        return False
Vamp=int(input('Digite um número com quatro dígitos:'))
if vampiro(Vamp):
    print('É vampiro!! =))')
else:
    print('Não é vampiro =((')