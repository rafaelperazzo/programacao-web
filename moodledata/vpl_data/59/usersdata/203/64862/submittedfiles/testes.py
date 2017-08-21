C=int(input('capital: '))
i=float(input('taxa: '))
i=i/100
tempo=int(input('tempo: '))
for t in range(1,tempo+1,1):
    juros=(1+i)**t
    total=C*juros
print(total)    