#criar um programa com 3 numeros e que o segundo maior seja exibido na tela.

numero1, numero2, numero3 = map(int, input().split())

meu_array = []

meu_array.append(numero1)
meu_array.append(numero2)
meu_array.append(numero3)

print(meu_array)

meu_array.sort() #essa função logica organiza os numeros pra vc.- 

print(meu_array)

print(meu_array [1] )


