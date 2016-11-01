# -*- coding: utf-8 -*-
from __future__ import division

a=input('Digite a: ')
b=input('Digite b: ')
c=input('Digite c: ')

q=c//a
i=c%a
d=c//b
e=c%b
if i%b==0: #Analisando a possibilidade do resto de "c" por "a" ser divisível por "b"
    print (q) 
    print(i//b)
elif e%a==0: #Se existir algum resto zero, então é possível existir a troca 
    print(e) #Caso "a" tenha resto diferente de zero e b tenha resto igual a zero
    print(d) #Em suma, analiza-se a possibilidade inversa da situação inicial
elif c%b==0 and c%a!=0: #Analisando os casos em que em que apenas b pode haver a troca
    print('0') #Se a não existe possibilidade de troca, então o 0 é mostrado
    print(c//b)
else: #Se todos os casos anteriores forem reprovados, então não existe a troca!
    print ('N')