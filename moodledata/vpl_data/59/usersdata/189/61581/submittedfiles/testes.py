n=int(input('valor:'))
i=0
while i*(i+1)*(i+2)>n:
    i=i+1
if i==n:
print ('sim')
print ('não')