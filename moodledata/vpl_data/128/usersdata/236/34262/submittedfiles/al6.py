# -*- coding: utf-8 -*
n=int(input('Digite o número:'))
for i in range(2,n,1):
    a=n%i
    if a==0:
        print (i)
        print ('Não primo')
    

