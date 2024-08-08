meu_dicionario = {
    1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}
}

meu_dicionario.update({
    2: {'nome': 'Paulo', 'idade': 21, 'nacionalidade': 'português'},
    3: {'nome': 'Leticia', 'idade': 19, 'nacionalidade': 'japones a'}
})

print(meu_dicionario)

copia_dicionario = meu_dicionario.copy()

elemento_removido = meu_dicionario.pop(1)
print(meu_dicionario)

ultimo_elemento_removido = meu_dicionario.popitem()
print(meu_dicionario)

meu_dicionario.clear()
copia_dicionario.clear()
print(meu_dicionario)
print(copia_dicionario)

chaves = [1, 2, 3]
novo_dicionario = dict.fromkeys(chaves, "Valor padrão")

print(novo_dicionario.items())

print(novo_dicionario.keys())

print("Valores do novo dicionário:", novo_dicionario.values())