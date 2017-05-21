n=int(input('n:'))
for i in range(1,n+1,1):
    l=int(input('l:'))
    r=int(input('r:'))
    d=int(input('d:'))
    if r>50 and l<r and r>d:
        print('s')
    else:
        print('n')