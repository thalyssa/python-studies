#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
var = float(input())

discount = var - (var * 0.05)

print('Novo preço com desconto: {:.2f}'.format(discount))
