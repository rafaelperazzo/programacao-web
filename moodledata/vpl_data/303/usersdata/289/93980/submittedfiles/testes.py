n = int(input("Digite um valor: "))
numeros=[]
for i in range (0,n,1):
    numeros.append(float(input("Digite o número%.d: " %(i+1))))
soma=0
for i in range (0,n,1):
    soma+=numeros[i]
media=soma/n
somatorio=0
for i in range (0,n,1):
    somatorio+=(numeros[i]-media)**2
desvPad=((1/(n-1))*somatorio)**(1/2)
print(desvPad)  
x=0
y=0
z=0
ddesvPad=2*desvPad
tdesvPad=3*desvPad
for i in range (0,n,1):
    p=numero[i]-media
    if p<desvPad:
        x+=1
    if p<ddesvPad:
        y+=1
    if p<tdesvPad:
        z+=1
if x/n==0.68 and y/n==0.95 and z/n==0.997:
    print("NORMAL")
else: 
    print("ANORMAL")
    
        
        
    