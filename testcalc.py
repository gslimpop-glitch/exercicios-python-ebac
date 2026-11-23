print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Escolha a opeação desejada")
num1 = float(input("digite o primeiro numero: "))
num2 = float(input("Digite o segundo numnero: "))
if opcao == "1":
    print("Resultado:", num1 + num2 ) 