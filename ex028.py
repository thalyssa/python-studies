#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(0, 5)
player = int(input("Digite um número de 0 a 5: "))

if player == num:
    print("Você acertou!")
else:
    print("Você errou. O número era: {}".format(num))

