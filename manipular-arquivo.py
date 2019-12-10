'''
arquivo = open("arquivo.txt")

texto_completo = arquivo.read()
print (texto_completo)


linhas = arquivo.readlines()

for linha in linhas:
	print(linha)
'''
w = open("arquivo2.txt", "w") # criar um novo arquivo

w.write("Acabei de criar este arquivo")

w.close()