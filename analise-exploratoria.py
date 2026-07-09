from itertools import count

import pandas as pd  # Manipulação e análise de dados
import matplotlib.pyplot as plt  # Criação de gráficos
import seaborn as sns  # Visualização de dados

## Filtrar colunas da planilha/base de dados ->
## Criar a variável para filtrar as colunas ->

colunas_desejadas = ["Player", "Pos", "Squad", "Comp", "Gls", "Ast", "G+A", "Saves", "Tkl+Int", "KP"]

## Ler dados de arquivos 'csv' ->
## Utilizar 'usecol' para utilizar a variável criada anteriormente ->

df = pd.read_csv(r"C:\pgm\projetos\analise-de-dados-ligas-europeias\players_data_light-2024_2025.csv", usecols=colunas_desejadas)

## Exibindo/Visualizando dados ->

print(df)

## Análise exploratória dos dados ->

## Total de gols ->

print("\nTotal de gols:")
print(sum(df["Gls"]))

## Quantidade de jogadores por liga ->

print("\nJogadores por liga:")
print(df["Comp"].value_counts())

## Total de posições em todas as ligas ->

print("\nPosições:")
print(df["Pos"].value_counts())

