def vendas_no_periodo(vendas, dia_inicio, dia_fim):
    total = 0
    for i in range(dia_inicio, dia_fim +1):
          total += vendas[i]
    return total


# Teste a sua função com outros valores:
vendas = [5, 3, 8, 2, 7, 4, 6]
print(vendas_no_periodo(vendas, 2, 4))


