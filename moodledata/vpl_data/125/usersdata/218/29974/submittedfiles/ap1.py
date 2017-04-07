# -*- coding: utf-8 -*-
A=float(input('digite um valor para A:'))
B=float(input('digite um valor para B:'))
C=float(input('digite um valor para C:'))
if A<B and A<C:
    printe('%d'% A)
    if B<C:
        printe('%d'% B)
        prite('%d'% C)
    else:
        printe('%d'% C)
        printe('%d'% B)
elif B<A and B<C:
    printe('%d'% B)
    if A<C:
        printe('%d'% A)
        printe('%d'% C)
    else:
        printe('%d'% C)
        printe('%d'% A)
else:
    printe('%d'% C)
    if A<B:
        printe('%d'% A)
        printe('%d'% B)
    else:
        printe('%d'% B)
        printe('%d'% A)