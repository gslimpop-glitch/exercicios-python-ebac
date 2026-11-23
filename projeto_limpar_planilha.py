import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

janela = tk.Tk()
janela.title("Limpador de Planilhas Automático")
janela.geometry("450x500")
janela.configure(bg="#f0f0f0")

tk.Label(janela, text="🧹 Limpador de Planilhas", font=("Arial", 18, "bold"), bg="#f0f0f0").pack(pady=15)
tk.Label(janela, text="Joga qualquer Excel sujo aqui que eu devolvo limpo!", bg="#f0f0f0").pack()

arquivo_escolhido = tk.StringVar()
tk.Label(janela, textvariable=arquivo_escolhido, bg="#f0f0f0", wraplength=400, fg="gray").pack(pady=10)

def escolher_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx *.xls")])
    if arquivo:
        arquivo_escolhido.set(arquivo)

def limpar_telefone(s):
    if pd.isna(s):
        return s
    so_numero = ''.join([c for c in str(s) if c.isdigit()])
    if len(so_numero) == 10:
        return f"({so_numero[:2]}) {so_numero[2:6]}-{so_numero[6:]}"
    if len(so_numero) == 11:
        return f"({so_numero[:2]}) {so_numero[2:7]}-{so_numero[7:]}"
    return s

def limpar():
    caminho = arquivo_escolhido.get()
    if not caminho:
        messagebox.showwarning("Ops!", "Escolha um arquivo primeiro!")
        return
    try:
        # 1. Ler
        df = pd.read_excel(caminho)
        linhas_antes = len(df)

        # 2. Tirar linhas totalmente vazias
        df = df.dropna(how='all')

        # 3. Limpar nome das colunas (tira espaço)
        df.columns = [str(c).strip() for c in df.columns]

        # 4. Limpar todas as colunas de texto (tira espaço e deixa primeira letra maiúscula)
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].astype(str).str.strip()
            # Se a coluna parecer telefone, formata
            if 'tel' in col.lower() or 'cel' in col.lower() or 'fone' in col.lower():
                df[col] = df[col].apply(limpar_telefone)
            # Se parecer nome, deixa bonito
            if 'nome' in col.lower():
                df[col] = df[col].str.title()

        # 5. Tentar converter colunas de data
        for col in df.columns:
            if 'data' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce', dayfirst=True)

        # 6. Tirar duplicados
        df = df.drop_duplicates()

        # 7. Salvar
        pasta = os.path.dirname(caminho)
        nome_novo = os.path.join(pasta, "planilha_LIMPA.xlsx")
        df.to_excel(nome_novo, index=False)

        linhas_depois = len(df)
        removidas = linhas_antes - linhas_depois

        messagebox.showinfo("Pronto! ✅", f"Limpeza concluída!\n\nAntes: {linhas_antes} linhas\nDepois: {linhas_depois} linhas\nRemovidas: {removidas} linhas sujas/duplicadas\n\nSalvo como:\nplanilha_LIMPA.xlsx")
    except Exception as e:
        messagebox.showerror("Erro", f"Deu erro: {e}")

tk.Button(janela, text="📂 ESCOLHER PLANILHA", command=escolher_arquivo, bg="#007AFF", fg="white", font=("Arial", 12, "bold"), height=2).pack(pady=10, padx=20, fill="x")
tk.Button(janela, text="✨ LIMPAR AGORA", command=limpar, bg="#28a745", fg="white", font=("Arial", 12, "bold"), height=2).pack(pady=10, padx=20, fill="x")

tk.Label(janela, text="O que ele faz:\n✅ Tira linhas vazias\n✅ Tira duplicados\n✅ Arruma telefones (11) 99999-9999\n✅ Arruma nomes e datas\n✅ Salva como planilha_LIMPA.xlsx", bg="#f0f0f0", justify="left").pack(pady=20)

janela.mainloop()