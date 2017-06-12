l=[]
cont=0
n=int(input('a'))
for i in range(1,n+1,1):
    a=int(input('a'))
    l.append(a)
for i in range(0,len(l)-1,1):
    if l[i]<l[i+1]:
        cont=cont+1
    if cont==(n-1):
        print('S')
    else:
        print('N')