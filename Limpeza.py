import pandas as pd

df = pd.read_excel("excel-transportadora-1787875824.xlsx")

# Tarefa 1: Custo total = Pedágio + Combustível + Outros custos
df['Custo total (R$)'] = df['Pedágio (R$)'] + df['Combustível (R$)'] + df['Outros custos (R$)']

# Tarefa 2: Margem em R$ = Frete - Custo total
df['Margem (R$)'] = df['Frete contratado (R$)'] - df['Custo total (R$)']

# Tarefa 3: Margem % = Margem / Frete * 100
df['Margem (%)'] = (df['Margem (R$)'] / df['Frete contratado (R$)'] * 100).round(2)

# Tarefa 4: Capacidade por tipo de veículo
# Tabela que todo mundo usa na transportadora
mapa_capacidade = {'VUC': 3500, 'Toco': 9000, 'Truck': 14000, 'Carreta': 30000}
df['Capacidade do veículo (kg)'] = df['Tipo de veículo'].map(mapa_capacidade)

# Tarefa 5: Ocupação % = Peso / Capacidade * 100
df['Ocupação (%)'] = (df['Peso da carga (kg)'] / df['Capacidade do veículo (kg)'] * 100).round(1)

# Tarefa 6: Entrega no prazo? Compara datas
def verifica_prazo(row):
    if pd.isna(row['Data efetiva de entrega']):
        return 'Pendente'
    return 'Sim' if row['Data efetiva de entrega'] <= row['Data prevista de entrega'] else 'Não'

df['Entrega no prazo?'] = df.apply(verifica_prazo, axis=1)

# Tarefa 7: Salva limpa
df.to_excel("transportadora_LIMPA.xlsx", index=False)
print("Pronto! Planilha limpa salva")
print(df[['ID da viagem','Margem (R$)','Margem (%)','Ocupação (%)','Entrega no prazo?']])