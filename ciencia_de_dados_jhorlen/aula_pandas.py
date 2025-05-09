import pandas as pd

dadosPromocoes = pd.read_csv("Contoso - Vendas - 2017.csv", delimiter=';', encoding='latin-1')

#Mostrando dados
#print(dadosPromocoes)   

#Mostra as informações
print(dadosPromocoes.info())

#Visualização
#print(dadosPromocoes['Data da Venda'])

#Mostra Linha e Coluna
print(dadosPromocoes[:3])

#
print(dadosPromocoes['Data da Venda'][0])