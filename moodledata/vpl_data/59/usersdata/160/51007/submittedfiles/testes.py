a=int(input('Digite um numero:'))
i=0
soma=0
while a>=0:
    resultado=a**2
    i=resultado//10
    r=resultado%10
    soma=soma+r
    resultado=resultado//10
print(soma)