#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO"

txt = input().strip()

if txt[:5].upper() == ('SANTO'):
	print('Começa')
else:
	print('Não começa')