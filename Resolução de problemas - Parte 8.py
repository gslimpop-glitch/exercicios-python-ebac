#Receba 1 numero e determine se ele é palindromo(le se igual ao contrario)
#receba o numero com o comando variavel int(input())
#transofrme o numero em string com o comando minha_string = str(variavel)

# meu_numero = int(input())

# minha_string = str(meu_numero)

# if minha_string == minha_string[::-1]:
#     print("É um palindromo")

# else:
#     print("Não é um palindromo")

numbers = [3, 1, 4]
numbers.sort()
second_largest = numbers[-2]
print(second_largest)