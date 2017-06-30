# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def vampiro(x):
    a=[]
    a.append(x//1000)
    x=x%1000
    a.append(x//100)
    x=x%100
    a.append(x//10)
    x=x%10
    a.append(x)
    
    
    if (a[0]*10+a[1])*(a[2]*10+a[3])=!x:
        return False
    elif (a[0]*10+a[1])*(a[2]+a[3]*10)!=x:
        return False
    elif (a[0]+a[1]*10)*(a[2]*10+a[3])!=x:
        return False
    elif (a[0]+a[1]*10)*(a[2]+a[3]*10)!=x:
        return False
    
    
    elif (a[0]*10+a[2])*(a[1]*10+a[3])!=x:
        return False
    elif (a[0]*10+a[2])*(a[1]+a[3]*10)!=x:
        return False
    elif (a[0]+a[2]*10)*(a[1]*10+a[3])!=x:
        return False
    elif (a[0]+a[2]*10)*(a[1]+a[3]*10)!=x:
        return False
    
    
    elif (a[0]*10+a[3])*(a[1]*10+a[2])!=x:
        return False
    elif (a[0]*10+a[3])*(a[1]+a[2]*10)!=x:
        return False
    elif (a[0]+a[3]*10)*(a[1]*10+a[3])!=x:
        return False
    elif (a[0]+a[3]*10)*(a[1]+a[2]*10)!=x:
        return False
    else:
        return True
Vamp=int(input('Digite um número com quatro dígitos:'))
if vampiro(Vamp):
    print('É vampiro!! =))')
else:
    print('Não é vampiro =((')