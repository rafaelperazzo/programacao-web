a= int(input('Digite um número: '))
b= int(input('Digite um número: '))
c= int(input('Digite um número: '))

if a > b and b > c :
    print('MAIOR:' a ', INTER:' b ', MENOR:' c )
elif a > c and c > b :
    print('MAIOR:' a ', INTER:' c ', MENOR:' b )
elif b > a and a > c :
    print('MAIOR:' b ', INTER:' a ', MENOR:' c )
elif b > c and c > a :
    print('MAIOR:' b ', INTER:' c ', MENOR:' a )
elif c > a and a > b :
    print('MAIOR:' c ', INTER:' a ', MENOR:' b )
elif c > b and b > a :
    print('MAIOR:' c ', INTER:' b ', MENOR:' a )
    
if a == b and b > c :
    print('MAIOR:' a ', INTER:' b ', MENOR:' c )
elif a == c and c > b :
    print('MAIOR:' a ', INTER:' c ', MENOR:' b )
elif b == c and c > a :
    print('MAIOR:' b ', INTER:' c ', MENOR:' a )
    
if a == b and b < c :
    print('MAIOR:' c ', INTER:' a ', MENOR:' b )
elif a == c and c < b :
    print('MAIOR:' b ', INTER:' c ', MENOR:' a )
elif b == c and c < a :
    print('MAIOR:' a ', INTER:' b ', MENOR:' c )

if a == b and c :
    print('MAIOR:' a ', INTER:' b ', MENOR:' c )