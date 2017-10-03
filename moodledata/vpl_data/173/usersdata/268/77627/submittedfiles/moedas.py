# -*- coding: utf-8 -*-
a=int(input('Digite o valor de a: '))
b=int(input('Digite o valor de b: '))
c=int(input('Digite o valor da cédula: '))
contador1=0
produtoa=1
cn=c
while((cn%b)==0)or((cn//b)==0):
    contador1=contador1 + 1
    protudoa= produtoa*a
    cn=c-produtoa
testeb=cn//b

if((produtoa + testeb*b)==c):
    print(contadora)
    print(testeb)
else:
    print('N')
