administrativo = ['Maria', 'Pedro', 'Evandro']
operacional = ['Augusta', 'Agatha', 'Gabriela']
tecnico = ['Marcela', 'Ygor', 'Cássia']

setores = {}
def uniao_setores(administrativo, operacional, tecnico):
    if len(administrativo)>2:
            setores['administrativo'] = tuple(administrativo)
    if len(operacional)>2:
            setores['operacional'] = tuple(operacional)
    if len(tecnico)>2:
            setores['tecnico'] = tuple(tecnico)
    return setores
# sort(setores)

def ordem_alfabetica(setores):
    nomes = list()
    for x in setores.values():
      for i in x:
            nomes.append(i)
    return sorted(nomes)


print(f"Setores {uniao_setores(administrativo, operacional, tecnico)}")
print(f" Nome dos participantes em ordem alfabética: {ordem_alfabetica(setores)}")

