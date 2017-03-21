N=input("digite a quantidade de quadrados da tira: ")
tira=[]
tira2=[]
cont=0
for i in range (0,N):
    num=input("digite -1 ou 0: ")
    tira.append(num)
    if num==0:
        cont=0
        tira2.append(cont)
    else:
        if cont<9:
            cont+=1
        tira2.append(cont)
print tira2
cont2=0
tira3=[]
for j in range(N-1,-1,-1):
    if tira[j]==0:
        cont=0
        tira3.insert(0,0)
    else:
        if cont2<9:
            cont2+=1
        tira3.insert(0,cont2)
print tira3
        
        

    

