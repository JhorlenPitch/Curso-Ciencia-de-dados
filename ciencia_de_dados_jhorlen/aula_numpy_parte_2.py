import numpy as np

array = np.array(np.random.randint(1, 10, 10))

print(array)

#Gerando Matrizes
print('Gerando Matrizes')
matriz_inteiros = np.array(np.random.randint(0, 2, size=(10, 10)))

print(matriz_inteiros)

#Verificando se tem valores vazios
print(np.isnan(array))


#Organizando em ordem
print('Em ordem: ', np.sort(array))

#Organizando em ordem decrescente
print('Em ordem: ', np.sort(array)[::-1])