import pandas as pd

contoso_produtos_df = pd.read_csv('Contoso - Cadastro Produtos.csv', delimiter=';', encoding='latin-1')
contoso_clientes_df = pd.read_csv('Contoso - Clientes.csv', delimiter=';', encoding='latin-1')
contoso_lojas_df = pd.read_csv('Contoso - Lojas.csv', delimiter=';', encoding='latin-1')
contoso_promocoes_df = pd.read_csv('Contoso - Promocoes.csv', delimiter=';', encoding='latin-1')
contoso_vendas_df = pd.read_csv('Contoso - Vendas - 2017.csv', delimiter=';', encoding='latin-1')

#print(contoso_produtos_df.info())
#print(contoso_clientes_df.info())
#print(contoso_lojas_df.info())
#print(contoso_promocoes_df.info())
#print(contoso_vendas_df.info())

print(contoso_clientes_df)

contoso_clientes_df.rename({'ID Cliente':'ID Cliente'})
novo_df = contoso_vendas_df.merge(contoso_clientes_df, on='ID Cliente')

print(novo_df)