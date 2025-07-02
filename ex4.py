
funcionario1 = {'nome': 'Vinicius', 'Cargo': 'Gerente', 'salario': 4500.50, 'subordinados': [{'nome': 'João', 'Cargo': 'Desenvolvedor Pleno', 'salario': 1500.50,},{'nome': 'Leticia', 'Cargo': 'Estagiária', 'salario': 1200.50}, {'nome': 'Chico', 'Cargo': 'Aprendiz', 'salario': 1000.50}]}
funcionario2 = {'nome': 'Ryan', 'Cargo': 'Músico', 'salario': 7300.50, 'subordinados': [{'nome': 'Matheus', 'Cargo': 'Pianista', 'salario': 2500.50,}]}
funcionario3 = {'nome': 'Marcio', 'Cargo': 'Dentista', 'salario': 2400.50, 'subordinados': [{'nome': 'Lucas', 'Cargo': 'Secretário', 'salario': 1400.50,}]}
funcionario4 = {'nome': 'Maria', 'Cargo': 'Médica', 'salario': 1000.50, 'subordinados': [{'nome': 'Pedro', 'Cargo': 'Enfermeiro', 'salario': 4500.50,}]}


print(len(funcionario1.get('subordinados')))
def total_folha(*args):
    soma_total_folha = 0
    soma_total_folha += funcionario1['salario']+ funcionario2['salario'] + funcionario3['salario']+ funcionario4['salario']
    print(f"Soma total da folha: R$ {soma_total_folha}")
    return total_funcionarios(*args)

def total_funcionarios(*args):
    total_funcionarios = len(args)+len(funcionario1.get('subordinados'))+ len(funcionario2.get('subordinados'))+len(funcionario3.get('subordinados'))+len(funcionario4.get('subordinados'))
    print(f"Soma total de funcionários: {total_funcionarios}")


def profundidade_hieraraquia():
    pass

total_folha(funcionario1,funcionario2,funcionario3,funcionario4)