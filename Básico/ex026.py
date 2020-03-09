#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input()).upper().strip()

print('O caractere A aparece {} vezes'.format(frase.count('A')))
print('Primeira aparição: {}'.format(frase.find('A')))
print('Última aparição: {}'.format(frase.rfind('A')))
