meu_array = [] #meu array é a sua lista de palavas (variavel)

for i in range(1,6): # for i in range() vai numerar de 1 a 5 as palavras (função)
    palavra = input() # input vai receber as palavras
    meu_array.append(palavra) # append vai adicionar as palavras recebidas na lista
    print('palavra sendo adicionada') #mostra na tela 


meu_array.sort() # o sort coloca em ordem

print(meu_array)    


