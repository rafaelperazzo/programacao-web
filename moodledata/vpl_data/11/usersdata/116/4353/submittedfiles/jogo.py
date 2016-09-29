# -*- coding: utf-8 -*-
from __future__ import division
import math

Cv = input ('insira a quantidade de vitórias do Cormengo:') 
Ce = input ('insira a quantidade de empates do Cormengo:') 
Cs = input ('insira o saldo de gols do Cormengo:') 
Fv = input ('insira a quantidade de vitórias do Flaminthians:') 
Fe = input ('insira a quantidade de empates do Flaminthians:') 
Fs = input ('insira o saldo de gols do Flaminthians:')

if Cv<Cf:
    print ('F')
if Cv>Cf:
    print ('C') 
if Cv==Cf:
    if Ce<Fe:
        print ('F') 
    if Ce>Fe:
        print ('C')
    if Ce==Fe: 
        if Cs<Fs:
            print ('F')
        if Cs>Fs:
            print ('C') 
        if Cs==Fs:
            print ('=')
    