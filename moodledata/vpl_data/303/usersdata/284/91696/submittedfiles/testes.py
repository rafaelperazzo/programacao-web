notas=[]
n=int(input('Digite n: '))
while n<=0:
    n=int(input('Digite n: '))

for i in range (0,n,1):
    notas.append(float(input('Digite a nota %d: ' % (i+1))))
media=0
for i in range (0,n,1):
    media += notas[i]/(n)
print(notas)

print(media)    




            
        

    
        
