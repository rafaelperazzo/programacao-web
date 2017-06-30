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
    denominador=calcula_fatorial(2)#Chama a função que irá calcular o fatorial do denominador da fórmula
    i=1
    while ((z**numerador)/denominador) >= epsilon:#Enquanto cada termo for maior que o valor mínimo que ele possa assumir...
        if i%2==0:#Se o termo for par...
            valorCosseno=valorCosseno+((z**numerador)/denominador)#Incrementa o valor do termo ao valor do Cosseno
        else:#Se o termo for ímpar...
            valorCosseno=valorCosseno-((z**numerador)/denominador)#Diminui o valor do termo no valor do Cosseno
        i=i+1
        numerador=numerador+2#Atualiza o valor do numerador
        denominador=calcula_fatorial(numerador)#É visível que o valor do denominador, é sempre igual ao fatorial do numerador, logo chamamos a função outra vez
    return(valorCosseno)#Retorna o valor aproximado do Cosseno

def razao_aurea(valorCosseno):#Inicia a função da Razão Áurea
    razaoAurea=2*(valorCosseno)
    return(razaoAurea)#Retorna o valor final da Razão Áurea

print('Olá usuário, seja bem vindo a plataforma de cálculo da Razão Áurea!\n')
print('Razão Áurea é \n')
print('Calculamos a razão áurea através de um método de aproximação bem preciso...\n')
print('Utilizamos uma aproximação do Cosseno de PI(3.1415926...) dividido por 5, e ao fim multiplicamos por 2!\n')
print('Para encontrar o valor de PI(3.1415926) utilizamos aproximações através de uma determinada quantidade de termos informados por você.\n')
m=int(input('Informe a quantidade de termos para estimar uma aproximação para o valor de PI: '))#Recebe o valor da quantidade de termospara a aproximação de PI
pi=calcula_pi(m)#Chama a função para calcular PI, e guarda o valor na váriável
print('Agora que temos um valor para aproximar PI, podemos calcular o Cosseno de PI/5, informando um valor mínimo para o valor de cada termo da fórmula.\n')
epsilon=float(input('Informe o valor mínimo para o cálculo do Cosseno: '))#Recebe o valor mínimo que um i-ésimo termo poderá atingir
print('Agora que temos todas as informações, podemos calcular o valor para PI, o Cosseno, e a Razão Áurea!\n')
z=(pi/5)#Z é a divisão de PI por 5
valorCosseno=calcula_co_seno(z,epsilon)#Chama a função para calcular o valor do Cosseno, informando o valor de Z e o valor mínimo dos termos
razao_aurea=razao_aurea(valorCosseno)#Chama a função apra calcular a Razão Áurea, informado o valor do Cosseno

print('Valor aproximado de PI: %.15f' %pi)#Imprime na tela o valor de PI
print('Valor aproximado de Cosseno: %.15f' %valorCosseno)#Imprime na tela o valor do Cosseno
print('Valor aproximado da Razão Áurea: %.15f' %razao_aurea)#Imprime na tela o valor da Razão Áurea
print('\n Com isso vemos que o valor é realmente próximo ao especulado!')
