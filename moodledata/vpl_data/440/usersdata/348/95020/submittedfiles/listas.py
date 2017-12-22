# -*- coding: utf-8 -*-

n = int(input('informe quantidade de termos: '))
while n < 2:
    n = int(input('informe quantidade de termos: '))
755
l1 = []

for i in range (0,n,1):
    l1.append(int(input('informe o %d° elemento da lista: ' %(i+1))))

if n == 7:
    a = l1[0] - l1[1]
    b = l1[1] - l1[2]
    c = l1[2] - l1[3]
    d = l1[3] - l1[4]
    e = l1[4] - l1[5]
    f = l1[5] - l1[6]
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


