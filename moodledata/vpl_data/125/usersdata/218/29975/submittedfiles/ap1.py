# -*- coding: utf-8 -*-
A=float(input('digite um valor para A:'))
B=float(input('digite um valor para B:'))
C=float(input('digite um valor para C:'))
if A<B and A<C:
    print('%d'% A)
    if B<C:
        print('%d'% B)
        print('%d'% C)
    else:
        print('%d'% C)
        print('%d'% B)
elif B<A and B<C:
    print('%d'% B)
    if A<C:
        print('%d'% A)
        print('%d'% C)
    else:
        print('%d'% C)
        print('%d'% A)
else:
    print('%d'% C)
    if A<B:
        print('%d'% A)
        print('%d'% B)
    else:
        print('%d'% B)
        print('%d'% A)