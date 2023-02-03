# Peço os valores e os armazeno em duas variáveis distintas
print("Insira dois valores!\n")
x = int(input("> "))
y = int(input("> "))

# Aqui dou várias opções e peço para escolher uma operação por seu número (assim facilita a codificação)
print("\nEscolha a operação: \n1- soma \n2- subtração \n3- divisão \n4- mutiplicação \n5- potenciação\n")

operacao = int(input("> "))
print()  #Esse print só usei para pular uma linha

# A partir do valor da variável 'operacao', eu realizo a operação matemática relacionada e já imprimo o resultado
if operacao == 1:
  print(x+y)

elif operacao == 2:
  print(x-y)

elif operacao == 3:
  print(x/y)

elif operacao == 4:
  print(x*y)

elif operacao == 5:
  print(x**y)

else:
  print("Opção indisponível")
