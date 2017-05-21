a=int(input('a:'))
maior=0
menor=a
for i in range(1,a+1,1):
    a=int(input('a:'))
    if a>maior:
        maior=a
    if a<menor:
        menor=a
print(maior)
print(menor)
    

