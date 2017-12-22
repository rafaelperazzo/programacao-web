# -*- coding: utf-8 -*-
m = int(input('Digite a quantidade de números: '))
m = []
m_i = []
m_p = []
for i in range(m):
    val = int(input('Digite um valor: '))
    m.append(val)
    if val%2 == 0 :
        m_p.append(val)
    if val%2 == 1 :
        m_i.append(val)
print(m)    
print(m_i) 
print(m_p) 