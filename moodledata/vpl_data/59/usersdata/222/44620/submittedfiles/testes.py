p=int(input('digite p: '))
q=int(input('digite q: '))
cont=0
i=0
temp=p
while temp>0:
    temp=temp//10
    i=i+1
while cont>0:
    resto=q%(10**i)
    if resto==p:
        cont=cont+1
    q=q//10
if cont>0:
    print('sim')
else:
    print('não')