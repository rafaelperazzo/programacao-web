n=int(input('n'))
for i in range(1,n+1,2):
    P=float(input('p:'))
    C=float(input('c:'))
    if (P*C)==(P*C):
        print('E')
    if  (P*C)>(P*C):
        print('-1')
    if  (P*C)<(P*C):
        print('1')    