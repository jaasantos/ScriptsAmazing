'''

# Biblioteca Random ######################################################################

Pseudo =>> números que podem ser repetidos em determinada fuçar

dir(random) => acessa todas funções e propriedades de random
Dir utilizando o dir

Função Random gera um numero pseudo aleatório entre 0 e 1

Import random => estou pedido para Python importar todo o modulo random
From random import random => estou pedindo para importar apenas a função do modulo random ; jeito mais leve e mais
recomendada de importar função de determinada biblioteca


for i in range():
    print(randint(1,61), end=', ')   # comece em 1 até 60, na mesma linha

    # import random
# Gerador de apostar da mega-sena
# from random import randint  => nao esta funcionando
# from random import shuffle

# funcao shuffle == funcao de embaralhar objetos


camisas_de_time = [ 1,2,3,4,5,6,7,8,9,10,11]
print(camisas_de_time)
shuffle(camisas_de_time)
print(camisas_de_time)

'''

import os

os.remove('legenda.txt')

