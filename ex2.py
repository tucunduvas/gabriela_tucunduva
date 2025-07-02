alunos = [('Lino', 7), ('Francisca',3), ('Ana Paula', 2), ('Matheus',1), ('Luisa', 3), ('Marcia', 4)]

def frequencia_maior_3(alunos):
    frequencia_3 = list(filter(lambda x: x[1]>=3, alunos))
    ativos = list(map(lambda x: x[0]+' - ativo', frequencia_3))
    return ativos


print(frequencia_maior_3(alunos))

