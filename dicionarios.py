meu_dicionario = {
    "codigo1": {"codigo": 1, "linguagem": "Python"},
    "codigo2": {"codigo": 2, "linguagem": "Java"},
    "codigo3": {"codigo": 3, "linguagem": "PHP"}
}

print(meu_dicionario)

print(type(meu_dicionario))


linguagem_codigo1 = meu_dicionario["codigo1"].get("linguagem")
print(linguagem_codigo1)

print(len(meu_dicionario))


dicionario_frutas = {
    1: {"nome": "limão", "tipo": "ácida"},
    2: {"nome": "laranja", "tipo": "ácida"},
    3: {"nome": "manga", "tipo": "semiácida"},
    4: {"nome": "maçã", "tipo": "semiácida"},
    5: {"nome": "banana", "tipo": "doce"},
    6: {"nome": "mamão", "tipo": "doce"}
}

print("Chave 1 - Nome:", dicionario_frutas[1]["nome"], ", Tipo:", dicionario_frutas[1]["tipo"])

print("Chave 2 - Nome:", dicionario_frutas[2]["nome"], ", Tipo:", dicionario_frutas[2]["tipo"])

for chave, valor in dicionario_frutas.items():
    print(f"Chave {chave} - Nome: {valor['nome']}, Tipo: {valor['tipo']}")

