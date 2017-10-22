# -*- coding: utf-8 -*-

investimento=float(input("Digite um valor: "))
taxa=float(input("Digite uma taxa: "))
while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

while investimento < investimento + (taxa*investimento):
    investimento= investimento + (taxa*investimento)