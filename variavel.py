S = 600.14
V = 806.76
C = 1370.47

investido = C - V
saldo_final = S - investido

print(f"Você vendeu: R$ {V}")
print(f"Sobrou investido: R$ {investido:.2f}")
print(f"Seu saldo agora: R$ {saldo_final:.2f}")

if saldo_final > 0:
    print("PARABÉNS! Você está POSITIVO e não paga juros!")
else:
    print("Ainda falta vender um pouco")