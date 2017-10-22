n=str(input('digite o número com 8 algarismos:'))
soma =0
if int( n)<10000000:
    print('NAO SEI')
if int( n)>99999999:
    print('NAO SEI')
for i in range (0,8,1):
    soma=soma + int(n[i])
print(soma)
