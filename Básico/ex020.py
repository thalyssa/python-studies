#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n1 = str(input())
n2 = str(input())
n3 = str(input())
n4 = str(input())
lista = [n1, n2, n3, n4]

random.shuffle(lista)
print(lista)