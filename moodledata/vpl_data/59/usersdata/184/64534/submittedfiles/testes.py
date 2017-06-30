p=int(input('Por favor amigo(a), digite seu peso:'))
h=int(input('Agora gostaríamos de saber sua altura:) :'))
imc= p/(h*h)
pi=(72.7*h)-58
if imc<= 18.4:
    print('Você está abaixo do peso. Talvez não esteja obtendo calorias o suficiente,adicione vitaminas e minerais a sua alimentação!')
    print('É importante lembrar que seu peso ideal é:%.1f'%pi)
else:
    if imc>=18.6 and imc<=24.9:
        print('Parabéns! Seu peso está normal. Mantenha-se assim, mas lenre da alimentação saudável!')
    elif imc>=25.0 and imc<=29.9:
        print('Ops, você está gordinho. Mas há formas de lidar com esse sobrepeso: combatendo a má alimentação e o sedentarismo, procure um especialista.')
        print('É importante lembrar que seu peso ideal é:%.1f'%pi)
    else:
        if imc>=30.0 and imc>=34.9:
            print('Eita, temos um problema! Você está com obesidade grau 1, mas que pode ser resolvida com muito esforço e foco na dieta, procure um especialista.')
            print('É importante lembrar que seu peso ideal é:%.1f'%pi)
        elif imc>=35.0 and imc<=39.9:
            print('Nossa! Você está com obesidade grau 2, mas não se desespere. Com a ajuda de um profissional e sua dedicação, você obterá bons resultados.')
            print('É importante lembrar que seu peso ideal é:%.1f'%pi)
        else:
            if imc>=40.0:
                print('Sinto informar, mas você está com obesidade grau 3. Sugerimos que procure um especialista, mantenha o foco na dieta e logo logo você sairá dessa!')
    