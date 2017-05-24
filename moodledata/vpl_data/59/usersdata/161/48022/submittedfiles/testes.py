n=int(input('numero:'))
for i in range(0,n,1):
    a=int(input('a'))
    maior=a
    menor=a
    if a>maior:
        maior=a
    if a<menor:
        menor=a
print(maior,menor)        