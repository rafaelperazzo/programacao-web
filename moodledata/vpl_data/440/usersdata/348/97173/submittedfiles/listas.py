# -*- coding: utf-8 -*-



n = int(input('informe quantidade de termos: '))
while n <= 2:
    n = int(input('informe quantidade de termos: '))

l1 = []

for i in range (0,n,1):
    l1.append(int(input('informe o %d° elemento da lista: ' %(i+1))))
'''
#testa depois esse codigo
for i in range (0,n,1):
    a = l1[i] - l1[i+1]
    if a < 0:
        a = a*(-1)
        if a > (l1[i]-l1[i+1]):
            print(a)
'''     
resultado = 0
for i in range (1, len(l1)):
    atual = abs(l1[i-1]-l1[i])
    if atual > resultado:
        resultado = atual
        
print(resultado)
    
'''    
if n == 7:
    a = abs(l1[0] - l1[1])
    b = abs(l1[1] - l1[2])
    c = abs(l1[2] - l1[3])
    d = abs(l1[3] - l1[4])
    e = abs(l1[4] - l1[5])
    f = abs(l1[5] - l1[6])

    if a < 0:
        a = a*(-1)
    if b < 0:
        b = b*(-1)
    if c < 0:
        c = c*(-1)
    if d < 0:
        d = d*(-1)
    if e < 0:
        e = e*(-1)
    if f < 0:
        f = f*(-1)

    if a > b and a > c and a > d and a > e and a > f:
        print(a)
    elif b > a and b > c and b > d and b > e and b > f:
        print(b)
    elif c > a and c > b and c > d and c > e and c > f:
        print(c)
    elif d > a and d > b and d > c and d > e and d > f:
        print(d)
    elif e > a and e > b and e > c and e > d and e > f:
        print(e)
    elif f > a and f > b and f > c and f > d and f > e:
        print(f)

if n == 5:
    j = l1[0] - l1[1]
    k = l1[1] - l1[2]
    l = l1[2] - l1[3]
    m = l1[3] - l1[4]
    
    if j < 0:
        j = j*(-1)
    if k < 0:
        k = k*(-1)
    if l < 0:
        l = l*(-1)
    if m < 0:
        m = m*(-1)

    if j > k and j > l and j > m:
        print(j)
    elif k > j and k > l and k > m:
        print(k)
    elif l > j and l > k and l > m:
        print(l)
    elif m > j and m > k and m > l:
        print(m)
    elif j == k == l == m:
        print(j)
        
'''