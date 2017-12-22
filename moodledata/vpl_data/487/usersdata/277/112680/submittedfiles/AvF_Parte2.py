# -*- coding: utf-8 -*-
"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
igual ao nome do usuário. Caso isso ocorra, o programa deve apenas pedir 
novamente a senha até que o usuário informe uma senha distinta do seu nome de 
usuário. Quando então o programa aceitar o nome de usuário e a senha informada, 
o programa deve apenas imprimir a palavra "ENTROU" (sem as aspas).

TEMPO ESTIMADO: 10 min
"""
user = input('user: ')
while True:
    pswd = input('pass: ')
    if (pswd != user):
        break
print("ENTROU")