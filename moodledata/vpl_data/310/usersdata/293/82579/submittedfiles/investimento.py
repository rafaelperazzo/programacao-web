# -*- coding: utf-8 -*-
from __future__ import division
saldo=0
investimento=float(input("Digite um valor: "))

while not(0<=taxa<=1):
    taxa=float(input("Digite uma taxa: "))

saldo=(investimento+(investimento*taxa)) 
while (True):
    