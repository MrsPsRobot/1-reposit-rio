def pares(i):
	if i % 2== 0:
		return i

def impar(i):
     if i % 2 == 1:
        return i
lista = [1,2,3,4,5,6,7,8,9,10]

lista_pares = filter(pares,lista)
lista_impar = filter(impar,lista)
print(list(lista_pares))
print(list(lista_impar))
separe = ("============================")
print(separe)

print("Usando a map")
def dobro(x):
	return x*2

valor = 2
vl_lista = [1,2,3]
print(dobro(valor))
print(dobro(vl_lista))
valor_dobrado = map (dobro, vl_lista)
valor_dobrado = list(valor_dobrado)
print(valor_dobrado)
print(separe)

print(dobro(valor))
print(dobro(vl_lista))
print("Imprimindo o dobro de cada item na lista com for")
valor_dobrado = map (dobro, vl_lista)
for v in valor_dobrado:
	print(v)

