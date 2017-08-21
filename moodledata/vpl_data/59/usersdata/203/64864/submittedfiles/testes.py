C=int(input('capital: '))
i=float(input('taxa: '))
i=(i/100)
t=int(input('tempo: '))
parcela=C/t
total=0
for m in range(1,t+1,1):
    total=total+parcela*i
print(total)