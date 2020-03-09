#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angle = float(input())

seno = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tg = math.tan(math.radians(angle))

print('{:.2f}\n{:.2f}\n{:.2f}'.format(seno, cos, tg))