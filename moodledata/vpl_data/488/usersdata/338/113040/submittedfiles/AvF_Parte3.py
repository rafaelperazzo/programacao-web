# -*- coding: utf-8 -*-
n = int(input('Digite a quantidade de números: '))
m = []
m_i = []
m_p = []

for i in range(0,n+1,1):
   m.append(0) 
for i in range(0,n+1,1):
   m_p.append(0) 
for i in range(0,n+1,1):
   m_i.append(0) 

for i in range(0,n+1,1):
    val = int(input('Digite um valor: '))
    if val != m[i]:
        m[i]=(val)
    if val%2 == 0 :
        if val != m_p[i]:
            m_p[i]=(val)
    if val%2 == 1 :
        if val != m_i[i]:
            m_i[i]=(val)
print(m)    
print(m_p) 
print(m_i) 