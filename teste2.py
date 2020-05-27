print ("telefones01=["'Tiago:",99999939, "Diego:",883874746, "Marta:",939939939]"com colchetes')
telefones01=["Tiago:",99999939, "Diego:",883874746, "Marta:",939939939, 'Orlando:',99169816]
print ("\nSo pode fazer inclusão um por vez com APPEND, telefones01.append("'Juse'")")
telefones01.append("Juse:")
telefones01.append(88776655)
print (telefones01)
print ("\nE para excluir com remove, telefones.remove("'Juse")"')
telefones01.remove("Juse:")
print (telefones01)
print ("\nTelefones com chaves{}")
telefones={"tiago":91991991,"diogo":92934567,"Marta":65542343}
print (telefones)
print ("\nE com {} pode fazer inclusão de varios com: telefones["'rita"]=94994999"\n')
telefones["rita"]=94994999
print (telefones)
print ("E para remover usa o del telefone["'tiago"]',"com colchete e apenas o nome e automaticamente o numero vai junto, pois foi criado juntos com :")
del telefones["tiago"]
print (telefones)



