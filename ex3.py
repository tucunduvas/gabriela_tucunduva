from random import randrange
from functools import reduce

def lista_1000():
    lista = [randrange(100,500) for _ in range(1000)]
    return total_a_pagar(lista, desconto_fixo = 100, desconto_percentual = 0.15)

def total_a_pagar(*args, **kwargs):
    total = int(reduce(lambda x,y: x+y, *args))
    desconto_porcentual = total*kwargs['desconto_percentual']
    total -= desconto_porcentual
    total -= kwargs['desconto_fixo']
    print(f'Total a pagar:  R$ {total}')

lista_1000()


