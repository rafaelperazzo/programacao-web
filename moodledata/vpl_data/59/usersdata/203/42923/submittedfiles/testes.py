n=int(input('digite n: '))
maior=0
menor=200
for i in range(0,n,1):
    idade=int(input('digite idade: '))
    if idade>maior:
        maior=idade
    if idade<menor:
        menor=idade
print(maior)
print(menor)