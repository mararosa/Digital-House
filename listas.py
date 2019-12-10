lista_frutas = ["abacaxi", "morango", "laranja", "melancia"]

'''
print(lista_frutas[2])
'''

tamanho =len(lista_frutas)
print (tamanho)
for item in lista_frutas:
	print(item)

#adicionar elementos na lista

lista_frutas.append("carambola")

print(lista_frutas)


if "uva" in lista_frutas:
	print ("Tenho uva na minha lista")
else:
	print ("Não tenho na lista")

del lista_frutas[3:]
print(lista_frutas)

#Ordenar a lista
lista_frutas.sort()
print(lista_frutas)

lista_frutas.sort(reverse = True)
print(lista_frutas)