#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math
co = float(input())
ca = float(input())

h = math.sqrt(math.pow(co, 2)+math.pow(ca, 2))
#math.hypot(co, ca)

print('{:.2f}'.format(h))