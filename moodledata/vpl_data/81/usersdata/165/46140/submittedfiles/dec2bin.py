# -*- coding: utf-8 -*-
p=int(input('digite p:'))
q=int(input('digite q:'))
variavel=p
i=0
while (variavel>0):
      variavel=variavel//10
      i=i+1

cont=0
while q>0:
    resto=q%(10**i)
    if resto==p:
        cont=cont+1
    q=q//10
    
if cont!=0:
    print('SIM')
else:
    print('NAO')


