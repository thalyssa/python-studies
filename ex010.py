#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere 1 dólar == 3,74 reais

real = float(input())
dols = real/3.74
print('US$: {:.2f}'.format(dols))
