menor=500
maior=0
for i in range(1,n+1,1):
    idade=int(input('digite a idade:'))
    if idade>maior:
        maior=idade
    if idade<menor:
        menor=idade