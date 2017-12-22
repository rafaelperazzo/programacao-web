# -*- coding: utf-8 -*-

n = int(input('informe quantidade de termos: '))
while n < 2:
    n = int(input('informe quantidade de termos: '))
755
l1 = []

for i in range (0,n,1):
    l1.append(int(input('informe o %d° elemento da lista: ' %(i+1))))

    if n == 7:
        a = lista[0] + lista[1]
        b = lista[1] + lista[2]
        c = lista[2] + lista[3]
        d = lista[3] + lista[4]
        e = lista[4] + lista[5]
        f = lista[5] + lista[6]
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


