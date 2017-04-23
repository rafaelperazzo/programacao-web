# -*- coding: utf-8 -*-
A=int(input('digite o primeiro num'))
B=int(input('digite o segundo num'))
C=int(input('digite o terceiro num'))
if (A<B) and (B<C):
    print (A)
    print (B)
    print (C)
elif (B<A) and (A<C):
    print (B)
    print (A)
    print (C)
elif (C<A) and (A<B):
    print (C)
    print (A)
    print (B)
elif (A<C) and (C<B):
    print (A)
    print (C)
    print (B)
elif (B<C) and (C<A):
    print (B)
    print (C)
    print (A)
elif (C<B) and (B<A):
    print (C)
    print (B)
    print (A)    

    