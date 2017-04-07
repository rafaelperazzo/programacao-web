A=float(input('Digite A:'))
B=float(input('Digite B:'))
C=float(input('digite C:'))
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
    

    
