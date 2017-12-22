# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de números: '))
m = []
m_i = []
m_p = []


for i in range(0,n,1):
    val = int(input('Digite um valor: '))
    m.append(val)
if val%2 == 0 :
    m_p.append(val)
if val%2 == 1 :
    m_i.append(val)

print(m)    
print(m_p) 
print(m_i) 