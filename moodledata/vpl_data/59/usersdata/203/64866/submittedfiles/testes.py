C=int(input('capital: '))
i=float(input('taxa: '))
i=(i/100)
t=int(input('tempo: '))
total=0
parcela=C/t
for m in range(1,t+1,1):
    total=total+parcela*(1+i)
print(total)