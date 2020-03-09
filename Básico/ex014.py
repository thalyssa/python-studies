#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
#TF = 1.8*TC + 32

celsius = float(input())
fah = (celsius*1.8)+32
print('{} °F'.format(fah))
