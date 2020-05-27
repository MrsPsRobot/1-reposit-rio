# -*- coding: utf8 -*-
minha_lista = ['Abacaxi','melancia','abacate']
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ['Abacaxi',2, 9.89, True]
separa =("==========================================================")

for inten in minha_lista:
	print(inten)

separa =("==========================================================")
print("Qual o tamanho ou numero de caracteres na lista?")
tam = len(minha_lista)
print(tam)
print(separa)

print("Adicionando elementos na lista")
minha_lista.append('limão')
print(minha_lista)
 
print(separa)
print("Existe o ... na lista?")
if (7 in minha_lista_2):
	print("7 está na lista")
else :
	print("Esse numero não está na lista")
print(separa)

print(minha_lista)
print("Removendo item. remova da lista do item 2 até o final")
del minha_lista[2:]
print(minha_lista)
print(separa)

print(minha_lista)
print("Apagando todos os itens da lista")
del minha_lista[:]
print(minha_lista)
print(separa)



