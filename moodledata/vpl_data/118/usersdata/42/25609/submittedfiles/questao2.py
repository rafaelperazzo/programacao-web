N=input("digite a quantidade de quadrados da tira: ")
tira=[]
tira2=[]
cont=0
cont3=0
for i in range (0,N):
    num=input("digite -1 ou 0: ")
    tira.append(num)
    if num==0:
        cont=0
        cont3+=1
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
        cont2=0
        tira3.insert(0,0)
    else:
        if cont2<9:
            cont2+=1
        tira3.insert(0,cont2)
print tira3
k=0
tira4=[]
while tira2[k]!=0:
    tira4.append(tira3[k])
    k+=1
cont4=0
while cont4<=cont3:
    if tira2[k]==0:
        tira4.append[k]
    elif tira2[k]<tira3[k]:
        tira4.append(tira2[k])
    else:
        tira4.append(tira3[k])
    k+=1
while k<len(tira):
    tira4.append(tira2[k])
    k+=1
print tira4
    
    
        
        

    

