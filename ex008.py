#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
var = float(input())
km = var/1000
hm = var/100
dam = var/10
dm = var*10
cm = var*100
mm = var*1000

print('km: {}\nhm: {}\ndam: {}\nm: {}\ndm: {}\ncm: {}\nmm: {}'.format(km, hm, dam, var, dm, cm, mm))