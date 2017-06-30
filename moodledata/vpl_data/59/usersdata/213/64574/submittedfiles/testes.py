def calcula_pi(m):#Inicia a função para calcular o valor de PI
    pi=3
    x=2
    for i in range(1,m+1,1):#Repetição que ajusta os termos para calcular o valor de PI
        if i%2==0:#Caso o termo seja par, ele descreve o valor...
            pi=pi-((4)/(x*(x+1)*(x+2)))
        else:#Caso o termo seja ímpar, ele acresce valor...
            pi=pi+((4)/(x*(x+1)*(x+2)))
        x=x+2
    return(pi)#Retorna o valor aproximado de PI

def calcula_fatorial(denominador):#Inicia a função para calcular o valor de um fatorial
    i=1
    fatorial=1
    while i<=denominador:#Enquanto o valor do número a ser calculado o fatorial, for maior que 1...
        fatorial=fatorial*i#Multiplica seu valor pela váriável...
        i=i+1#A variável é acrescida de um...
    return(fatorial)#Retorna o valor final do fatorial

def calcula_co_seno(z,epsilon):#Inicia a função Cosseno, informando Z(PI/5) e epsilon(valor mínimo que cada termo pode assumir)
    valorCosseno=1
    numerador=2
    denominador=calcula_fatorial(2)#Chama
    i=1
    while ((z**numerador)/denominador) >= epsilon:
        if i%2==0:
            valorCosseno=valorCosseno+((z**numerador)/denominador)
        else:
            valorCosseno=valorCosseno-((z**numerador)/denominador)
        i=i+1
        numerador=numerador+2
        denominador=calcula_fatorial(numerador)
    return(valorCosseno)

def razao_aurea(valorCosseno):
    razaoAurea=2*(valorCosseno)
    return(razaoAurea)

print('Olá usuário, seja bem vindo a plataforma de cálculo da Razão Áurea!')
print('Razão Áurea é')
print('Calculamos a razão áurea através de um método de aproximação bem preciso...')
print('Utilizamos uma aproximação do Cosseno de PI(3.1415926...) dividido por 5, e ao fim multiplicamos por 2!')
print('Para encontrar o valor de PI(3.1415926) utilizamos aproximações através de uma determinada quantidade de termos informados por você.')
m=int(input('Informe a quantidade de termos para estimar uma aproximação para o valor de PI: '))
pi=calcula_pi(m)
print('Agora que temos um valor para aproximar PI, podemos calcular o Cosseno de PI/5, informando um valor mínimo para o valor de cada termo da fórmula.')
epsilon=float(input('Informe o valor mínimo para o cálculo do Cosseno: '))
print('Agora que temos todas as informações, podemos calcular o valor para PI, o Cosseno, e a Razão Áurea! ')
z=(pi/5)
valorCosseno=calcula_co_seno(z,epsilon)
razao_aurea=razao_aurea(valorCosseno)

print('Valor aproximado de PI: %.15f' %pi)
print('Valor aproximado de Cosseno: %.15f' %valorCosseno)
print('Valor aproximado da Razão Áurea: %.15f' %razao_aurea)
