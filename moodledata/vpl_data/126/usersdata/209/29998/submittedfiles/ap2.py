# -*- coding: utf-8 -*-
A=int(input('digite o valor A:'))
B=int(input('digite o valor B:'))
C=int(input('digite o valor C:'))
D=int(input('digite o valor D:'))
if A>=B and A>=C and A>=D:
    print(A)
    if B<=C and B<=D:
        print(B)
    elif C<=B and C<=D:
        print(C)
    elif D<=B and D<=C:
        print(D)
elif B>=A and B>=C and B>=D:
    print(B)
    if A<=C and A<=D:
        print(A)
    elif C<=A and C<=D:
        print(C)
    elif D<=A and D<=C:
        print(D)
elif C>=A and C>=B and C>=D:
    print(C)
    if A<=B and A<=D:
        print(A)
    elif B<=A and B<=D:
        print(B)
    elif D<=A and D<=B:
        print(D)
elif D>=A and D>=B and D>=C:
    print(D)
    if A<=B and A<=C:
        print(A)
    elif B<=A and B<=C:
        print(B)
    elif C<=A and C<=B:
        print(C)