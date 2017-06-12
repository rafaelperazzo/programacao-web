def calc_pi(m):
    soma=0
    denominador=2
    for i in range(1,m+1):
        if i%2==1:
            soma=soma+(4/float((denominador)*(denominador+1)*(denominador+2)))
        else:
            soma=soma-(4/float((denominador)*(denominador+1)*(denominador+2)))
        denominador=denominador+2
    pi=2+soma
    return(pi)
    
    print(calcula_pi(100))
            