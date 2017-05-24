n=int(input('numero:'))
maior=0
menor=a
for i in range(0,n,1):
    a=int(input('a'))
    if a>maior:
        maior=a
    if a<menor:
        menor=a
print(maior,menor)        