# -*- coding: utf-8 -*-
a=[]
b=[]
c=[]
n=int(input('Digite o número de elementos: '))
while n<=0:
    print('Número inválido!')
    n=int(input('Digite o número de elemento: '))
for i in range(0,n,1):
    a.append(input('Digite um elemento para a: '))
for j in range(0,n,1):
    b.append(input('Digite um elemento para b: '))
for k in range(0,n,1):
    c.append(input('Digite um elemento para c: '))
g=[]
o=[]
p=[]
q=sorted(a)
for l in range(0,n,1):
    if (l+1) == n:
        break
    if a[l]<a[l+1]:
        g.append(a[l])
        if l == n-2:
            g.append(a[l+1])
    if a[l]>a[l+1]:
        o.append(a[l])
        if l == n-2:
            o.append(a[l+1])
    if q[l]==q[l+1]:
        p.append(q[l])
s=[]
m=[]
x=[]
z=sorted(b)
for w in range(0,n,1):
    if (w+1) == n:
        break
    if b[w]<b[w+1]:
        s.append(b[w])
        if w == n-2:
            s.append(b[w+1])
    if b[w]>b[w+1]:
        m.append(b[w])
        if w == n-2:
            m.append(b[w+1])
    if z[w]==z[w+1]:
        x.append(z[w])
d1=[]
d2=[]
d3=[]
d4=sorted(c)
for y in range(0,n,1):
    if(y+1) == n:
        break
    if c[y]<c[y+1]:
        d1.append(c[y])
        if y == n-2:
            d1.append(c[y+1])
    if c[y]>c[y+1]:
        d2.append(c[y])
        if y == n-2:
            d2.append(c[y+1])
    if d4[y]==d4[y+1]:
        d3.append(d4[y])
if len(g) == len(a):
    print('S')
if len(o) == len(a):
    print('N')
if len(p) + len(g) == len(a):
    print('S')
if len(p) + len(o) == len(a):
    print('N')
if len(s) == len(b):
    print('S')
if len(m) == len(b):
    print('N')
if len(x) + len(s) == len(b):
    print('S')
if len(x) + len(m) == len(b):
    print('N')
if len(d1) == len(c):
    print('S')
if len(d2) == len(c):
    print('N')
if len(d3) + len(d1) == len(c):
    print('S')
if len(d3) + len(d2) == len(c):
    print('N')
if len(g) == len(a):
    print('N')
if len(o) == len(a):
    print('S')
if len(p) + len(g) == len(a):
    print('N')
if len(p) + len(o) == len(a):
    print('S')
if len(s) == len(b):
    print('N')
if len(m) == len(b):
    print('S')
if len(x) + len(s) == len(b):
    print('N')
if len(x) + len(m) == len(b):
    print('S')
if len(d1) == len(c):
    print('N')
if len(d2) == len(c):
    print('S')
if len(d3) + len(d1) == len(c):
    print('N')
if len(d3) + len(d2) == len(c):
    print('S')

    
    

    
