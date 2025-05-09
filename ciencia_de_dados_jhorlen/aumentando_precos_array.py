import numpy as np

#criando um array de inteiros
precos = np.array([20,40,25,35,30])
print(precos)

#Aumento o preço de todos os valores do array em 10%
novos_precos = precos * 1.1
print(f'Valor aumentando: {novos_precos}!')

#Soma de todos os precos do array precos
total_vendas = np.sum(precos)
print(f'Soma de todos os valores do array: {total_vendas}!')

#Média dos preços
media_precos = np.mean(precos)
print(f'A média dos preços é {media_precos}!')

#Maior e menor valor
maior_valor = np.max(precos)
menor_valor = np.min(precos)

print(f'O maior valor é {maior_valor}!')
print(f'O menor valor é {menor_valor}!')

#Lista 

k = list(range(1,10))
print(k)

rng = np.random.default_rng()

print(rng.random(4_0))

array_aleatorio = np.array(rng.random(500_000) * 4_00)

maior = np.max(array_aleatorio)
maior_arredondado = round(maior, 1)

menor = np.min(array_aleatorio)
menor_arredondado = round(menor, 1)

media = np.mean(array_aleatorio)
media_arredondado = round(media, 1)

print(f'O maior é {maior_arredondado}.')
print(f'O menor é {menor_arredondado}.')
print(f'A média é {media_arredondado}.')