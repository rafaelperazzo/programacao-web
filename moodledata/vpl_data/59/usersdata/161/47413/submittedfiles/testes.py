n=int(input('n:'))
maior=0
menor=0
for i in range(1,n+1,1):
    a=int(input('a:'))
    if a>maior:
        maior=a
    if a<menor:
        menor=a
print(maior)
print(menor)
    

