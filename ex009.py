#Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada
var = int(input())
#range(start, stop, step)
for i in range(1, 11, 1):
    print('{} x {:2} = {}'.format(var, i, var*i))
