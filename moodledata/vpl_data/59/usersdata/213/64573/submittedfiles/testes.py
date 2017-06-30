def calcula_pi(m):
    pi=3
    x=2
    for i in range(1,m+1,1):
        if i%2==0:
            pi=pi-((4)/(x*(x+1)*(x+2)))
        else:
            pi=pi+((4)/(x*(x+1)*(x+2)))
        x=x+2
    return(pi)

def calcula_fatorial(denominador2):
    i=1
    fatorial=1
    while i<=denominador2:
        fatorial=fatorial*i
        i=i+1
    return(fatorial)

def calcula_co_seno(z,epsilon):
    valorCosseno=1
    denominador1=2
    denominador2=calcula_fatorial(2)
    i=1
    while ((z**denominador1)/denominador2) >= epsilon:
        if i%2==0:
            valorCosseno=valorCosseno+((z**denominador1)/denominador2)
        else:
            valorCosseno=valorCosseno-((z**denominador1)/denominador2)
        i=i+1
        denominador1=denominador1+2
        denominador2=calcula_fatorial(denominador1)
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
