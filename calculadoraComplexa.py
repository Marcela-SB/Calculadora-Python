print("Insira uma conta matemática!    EX: 2 * 3")
print("(PS: deixe um espaço entre os itens)\n")

# Aqui eu obtenho os valores das variáveis em apenas uma linha e o '.split("")' distribui elas para cada variável. Mas isso só é possível se houver um espaço entre cada ítem.
x,operacao,y = input().split()

# Converto os valores das variáveis para os tipos que preciso
x = int(x)
operacao = str(operacao)
y = int(y) 

print("\nRESULTADO:")

# A partir do valor da variável 'operacao', eu realizo a operação matemática relacionada e já imprimo o resultado
if operacao == "+":
  print(x+y)

elif operacao == "-":
  print(x-y)

elif operacao == "/":
  print(x/y)

elif operacao == "*":
  print(x*y)

elif operacao == "**":
  print(x**y)

else:
  print("Opção indisponível")
