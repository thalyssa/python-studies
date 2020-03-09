#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
w = float(input())
h = float(input())

area = w*h
qtdInk = area/2

print('Área: {:.2f}m²\nTinta: {:.2f}l'.format(area, qtdInk))