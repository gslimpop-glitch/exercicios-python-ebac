# def process_data(data):
#     processed_data = []
#     for item in data:
#         if isinstance(item, int) and item > 0:
#             processed_data.append(item * 2)
#         elif isinstance(item, str):
#             processed_data.append(item.upper())
#     return processed_data

# data = [1, 'hello', -3, 'world', 5]
# result = process_data(data)
# print(result)

def calcular_frete(valor_compra, cliente_vip):
    if cliente_vip or valor_compra >= 100:
        return 0
    elif valor_compra >= 50:
        return 9.9
    else:
        return 19.9

print(calcular_frete(75.0, False))    