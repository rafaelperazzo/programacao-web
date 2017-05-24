base=int(input('digite a base:'))
expoente=int(input('digite o expoente:'))
cont=0
produto=1
while cont<expoente:
    produto=produto*base
    cont=cont+1
print(base 'elevado a',expoente, '=',produto)