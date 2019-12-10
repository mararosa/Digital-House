
"""
a = "Mara"
b = "Rosa" 

concatenar = a + " " + b + "\n" 
print(concatenar)
print(concatenar.lower())
print(concatenar.upper())  # posso fazer assim tb, concatenar = concatenar.upper()

tamanho = len(concatenar)
print (tamanho)

print(a[2]) #posição indice começa do 0

print (concatenar[0:4])

"""

#função split convert sequencia em lista

texto = "Estou muito feliz e grata!"

texto = texto.replace("grata", "animada")
print (texto)

busca = texto.find("feliz")
print(busca)

print(texto[busca:])  #pegar todo o trecho que vem depois de feliz

lista = texto.split("e")
print (lista)


