# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
A= int(input('Digite A: '))
B= int(input('Digite B: '))
C= int(input('Digite C: '))
D= int(input('Digite D: '))
if A>B>C>D or A>C>B>D:
    print(A)
    print(D)
if B>C>D>A or B>D>C>A:
    print(B)
    print(A)
if C>D>A>B or C>A>D>B:
    print(C)
    print(B)
if D>A>B>C or D>B>A>C:
    print(D)
    print(C)
if A<B<C<D or A<C<B<D:
    print(D)
    print(A)
if B<C<D<A or B<D<C<A:
    print(A)
    print(B)
if C<D<A<B or C<A<D<B:
    print(B)
    print(C)
if D<A<B<C or D<B<A<C:
    print(C)
    print(D)
if A>B>D>C or A>D>B>C:
    print(A)
    print(C)
if B>C>A>D or B>A>C>D:
    print(B)
    print(D)
if C>D>B>A or C>B>D>A:
    print(C)
    print(A)
if D>A>C>B or D>C>A>B:
    print(D)
    print(B)