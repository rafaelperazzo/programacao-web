n=int(input('n'))
for i in range(1,n+1,1):
    a=int(input('a'))
    cont=0
    for j range(2,a+1,1):
        if a%j==0:
            cont=cont+1
        if cont==0:
            print('primo')
        else:
            print('nao primo')
        