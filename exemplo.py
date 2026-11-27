import pandas as pd

idades_lista = [25, 30, 22, 28]

idades_series = pd.Series([25, 30, 22, 28])

# print(f"lista: \n{idades_lista}\n")
# print(f"lista: \n{idades_series}\n")

# Manipulando Series e Consultas
notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana']) 

 

print(notas['Maria'])       # Acessando a nota da Maria pelo rótulo 

print(notas.iloc[2])        # Acessando a nota de Pedro pela posição 

print(notas.mean())         # Calculando a média das notas 

print(notas[notas > 8])     # Filtrando notas maiores que 8 

print(notas.describe())     # Estatísticas descritivas das notas 

# Aumentar todas as notas em 10% de uma vez só 

notas_ajustadas = notas * 1.10 

print(notas_ajustadas) 

# Comparar com uma segunda series 

notas_exame_final = pd.Series([10, 7.5, 8.0, 9.5], index=['João', 'Maria', 'Pedro', 'Ana']) 

diferenca = notas_exame_final - notas_ajustadas 

 
print(diferenca)
#Dataframes: lendo planilhas do Excel

df = pd.read_excel('base_invest.xlsx')  # lê a planilha Excel da Pasta

print(df.head())                       # Exibe as 5 primeiras linhas
# Abrir abas de planilhas do excel diferentes 

df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes') 

 

df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo') 

 

print(df_transacoes.head()) 

print(df_ativo.head()) 


