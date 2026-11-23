# import tkinter as tk

# janela = tk.Tk()
# janela.title("Calculadora Bolsa - Não fica negativo")
# janela.geometry("380x380")
# janela.configure(bg="#f0f0f0")

# # Título
# tk.Label(janela, text="Calculadora da Íon", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)

# # Função para criar caixinha + texto
# def criar_campo(texto, valor_inicial):
#     tk.Label(janela, text=texto, bg="#f0f0f0", anchor="w").pack(fill="x", padx=20)
#     entrada = tk.Entry(janela, font=("Arial", 12))
#     entrada.insert(0, valor_inicial)
#     entrada.pack(pady=5, padx=20, fill="x")
#     return entrada

# entrada_saldo = criar_campo("1. Quanto você tem na conta (R$):", "600.14")
# entrada_comprei = criar_campo("2. Quanto você comprou hoje (R$):", "1370.47")
# entrada_vendi = criar_campo("3. Quanto você já vendeu hoje (R$):", "806.76")

# # Área do resultado
# resultado_texto = tk.Label(janela, text="", font=("Arial", 11), bg="#f0f0f0", justify="left")
# resultado_texto.pack(pady=15)

# def calcular():
#     try:
#         saldo = float(entrada_saldo.get().replace(",", "."))
#         comprei = float(entrada_comprei.get().replace(",", "."))
#         vendi = float(entrada_vendi.get().replace(",", "."))
        
#         investido = comprei - vendi
#         saldo_final = saldo - investido
        
#         if saldo_final >= 0:
#             msg = f"Investido: R$ {investido:.2f}\nSaldo final: R$ {saldo_final:.2f}\n\n✅ ESTÁ POSITIVO! Não paga juros."
#             cor = "green"
#         else:
#             falta = abs(saldo_final)
#             msg = f"Investido: R$ {investido:.2f}\nSaldo final: R$ {saldo_final:.2f}\n\n❌ FALTA VENDER R$ {falta:.2f} ainda!"
#             cor = "red"
            
#         resultado_texto.config(text=msg, fg=cor)
#     except:
#         resultado_texto.config(text="Digite só números! Use ponto ou vírgula.", fg="orange")

# tk.Button(janela, text="CALCULAR AGORA", command=calcular, bg="#007AFF", fg="white", font=("Arial", 12, "bold"), height=2).pack(pady=10, padx=20, fill="x")

# janela.mainloop()
# ConnectionAbortedErrorar
# classmethod
# Para o Init: Em vez de apenas poetry init, precisei usar py -m poetry init.
Para o Shell (Ambiente Virtual): Aqui precisei de dois passos adicionais:
Primeiro, instalei o plugin com: pip install poetry-shell
Depois, para ativar a máquina virtual, o comando que funcionou foi: py -m poetry shell