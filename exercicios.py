#Exercicio 1
'''
idade = int(input("Digite sua idade: "))

if idade >= 18:
	print ("Já pode ser preso")

elif idade > 0 and idade < 18:
	print ("Você é menor de idade")

else:
	print ("Idade inválida")
	'''


#Exercicio 2

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print (media)

if media >= 6:
	print ("Sua média é %f" %(media) + " Aprovado")

else:
	print ("Sua média é: %f" %(media) + " Reprovado")
