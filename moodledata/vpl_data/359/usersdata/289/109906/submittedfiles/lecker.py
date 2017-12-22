n=int(input("Digite a quantidade de elementos das listas: "))
lista_1=[]
lista_2=[]
for i in range (0,n,1):
    lista_1.append(int(input("Digite o elemento%.d da lista 1: " %(i+1))))
for i in range (0,n,1):
    lista_2.append(int(input("Digite o elemento%.d da lista 2: " %(i+1))))
c=0
for i in range(0,n,1):
    if i==0:
        if lista_1[0]>lista_1[1]:
            c+=1
    if i==n:
        if lista_1[i]>lista_1[i-1]:
            c+=1
    if i!=0 or i!=n:
        if lista_1[i-1]<lista_1[i]>lista_1[i+1]:
if c==1:
    print("S")
else:
    print("N")
d=0
for i in range(0,n,1):
    if i==0:
        if lista_2[0]>lista_2[1]:
            d+=1
    if i==n:
        if lista_2[i]>lista_2[i-1]:
            d+=1
    if i!=0 or i!=n:
        if lista_2[i-1]<lista_2[i]>lista_2[i+1]:
            d+=1
if d==1:
    print("S")
else:
    print("N")
