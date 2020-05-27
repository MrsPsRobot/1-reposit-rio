arq3 = open("arquivo3.rtf","w")
arq3.write("Conteudo do novo arquivo3\nsegunda linha do file")
arq3.close()
#abrindo arquivo por linhas
arquivo3 = open("arquivo3.rtf")
modabr = arquivo3.readlines()
print(modabr)
for modabr in modabr:
	print(modabr)

w = open("arquivo.txt","a")
w.write("\nConteudo do novo arquivo2")
w.close()
arquivo = open("arquivo.txt")
abrarq = arquivo.read()
print(abrarq)


w = open("arquivo2.txt","w")
w.write("Esse é novo do novo\nDnovo no novo")
w.close()
arquivo2 = open("arquivo2.txt")
abrarq = arquivo2.read()
print(abrarq)


