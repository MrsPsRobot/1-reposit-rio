separa = ("================================================")
meu_dicionario = {'A':'Ameixa','B':'bola','C':'cachorro'}
print(meu_dicionario["A"])
print(meu_dicionario)
print(separa)

for chave in meu_dicionario:
	print(chave)
print(separa)
for chave in meu_dicionario:
	print(chave+"-"+meu_dicionario[chave])
	

for  i in meu_dicionario.items():
		print(i)
       

for  i in meu_dicionario.values():
			print(i)

for k in meu_dicionario.keys():
	print(k)

