a = float(input('Digite um número: '))

if a%3 == 0 and a%7==0:
    print('é divisível')
if a%3 != 0 or a%7!=0 :
    print('Não é')