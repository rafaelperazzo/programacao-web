# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
def vampiro(x):
    a=[]
    y=x
    a.append(y//1000)
    y=y%1000
    a.append(y//100)
    y=y%100
    a.append(y//10)
    y=y%10
    a.append(y)
    
    
    if ((a[0]*10)+a[1])*((a[2]*10)+a[3])==x:
        return True 
    elif (a[0]*(10+a[1]))*(a[2]+(a[3]*10))==x:
        return True 
    elif (a[0]+(a[1]*10))*((a[2]*10)+a[3])==x:
        return True 
    elif (a[0]+a[1]*10)*(a[2]+(a[3]*10))==x:
        return True 
    elif (a[0]*10+a[2])*(a[1]*10+a[3])==x:
        return True 
    elif (a[0]*10+a[2])*(a[1]+a[3]*10)==x:
        return True 
    elif (a[0]+a[2]*10)*(a[1]*10+a[3])==x:
        return True 
    elif (a[0]+a[2]*10)*(a[1]+a[3]*10)==x:
        return True 
    
    
    elif (a[0]*10+a[3])*(a[1]*10+a[2])==x:
        return True 
    elif (a[0]*10+a[3])*(a[1]+a[2]*10)==x:
        return True 
    elif (a[0]+a[3]*10)*(a[1]*10+a[3])==x:
        return True 
    elif (a[0]+a[3]*10)*(a[1]+a[2]*10)==x:
        return True
    else:
        return False 
Vamp=int(input('Digite um número com quatro dígitos:'))
if vampiro(Vamp)==True:
    print('É vampiro!! =))')
else:
    print('Não é vampiro =((')