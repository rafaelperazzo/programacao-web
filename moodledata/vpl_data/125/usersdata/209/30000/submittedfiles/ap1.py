A=int(input('Digite A:'))
B=int(input('Digite B:'))
C=int(input('digite C:'))
if A<=B and A<=C:
    print(A)
    if B<=C:
        print(B)
        print(C)
    else:
        print(C)
        print(B)
elif B<=A and B<=C:
    print(B)
    if A<=C:
        print(A)
        print(C)
    else:
        print(C)
        print(A)
elif C<=A and C<=B:
    print(C)
    if B<=A:
        print(B)
        print(A)
    else:
        print(A)
        print(B)


    
