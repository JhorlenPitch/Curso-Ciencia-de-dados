#Importando a biblioteca
import numpy as np

#Criando um array de letras
array_letras = np.array(['a', 'b', 'c', 'd', 'e'])

print(array_letras)

#Acessando valor pela chave
print(array_letras[0])

#Acessando um intervalo, não inclui o '2', no caso quero imprimir 3, coloco 0:4
print(array_letras[0:2])

#meu_array = np.array([1,2,3,4,5])

#print(meu_array)

#print(meu_array.shape)

#my_array = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]) 

#print(my_array)
#print(my_array.shape)

#a = np.arange(6).reshape((3, 2))
#print(a)