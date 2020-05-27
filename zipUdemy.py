lista = [1,2,3,4,5,6]
lista2 = ["abacate","bola","cachorro","dinheiro","elefante","fusca"]
lista3 = ["R$2.00","R$3.00","R$2.30","R$2.50","R$3.00","R$2.20"]

for numero,nome,pr in zip(lista,lista2,lista3):
	print(numero,nome,pr)