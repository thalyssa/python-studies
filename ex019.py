#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

n1 = input()
n2 = input()
n3 = input()
n4 = input()

list = [n1, n2, n3, n4]

target = random.choice(list)

print('{}'.format(target))