#EXERCICIO 1
#n= int(input('Digite quantos lados deve ter o seu polígono: '))
#nd= (n*(n-3))/2
#print('%.1f' % nd)

#EXERCÍCIO 2
#f= float(int('Digite um valor para f: '))
#L= float(int('Digite um valor para L: '))
#Q= float(int('Digite um valor para Q: '))
#DeltaH= float(int('Digite um valor para DeltaH: '))
#v= float(int('Digite um valor para v: '))
#g= 9.81
#libra= 0.000002
#pi= (math.pi)

#D= ((8*f*L*(Q**2))/((pi**2)*g*DeltaH))**(1/5)
#Rey= (4*Q)/(pi*D*v)
#k= (0.25)/((match.log10((libra)/(3*D))+((5.74)/(Rey**0.9)))**2)

#print('%.4f' % D)
#print('%.4f' % Rey)
#print('%.4f' % k)

#EXERCICIO 6
#a= float(input('Digite um valor para a: '))
#b= float(input('Digite um valor para b: '))
#c= float(input('Digite um valor para c: '))

#Delta= b**2-4*a*c
#raizDelta= (Delta)**0.2
#x1= (-b+raizDelta)/(2*a)
#x2= (-b-raizDelta)/(2*a)

#if Delta < 0:
 #   print('SRR')
#else:
  #  print('%.2f' % x1)
 #   print('%.2f' % x2)
    
#EXERCICIO 7
#Valor a ser sacado= int(input("Digite o valor a ser sacado: "))
#vs==Valor a ser sacado

'''
n= int(input('Digite o valor de n: '))
i=1
cont=0
while (i<n):
    if i%2==1:
        cont= cont+1
    i= i+1
print (cont)
'''

i=1
n= int(input('Digite o valor de n: '))
while (n<=0):
    n= int(input('Digite o valor de n: '))
while (i<=n):
    print(i**2)
    i=i+2