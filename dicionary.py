dicionario= {
    "chave_valor":  "result",  #chave_valor armazena o conteudo "result"
    "linguagem":  "c#",
    "sonho":  "desenvolvedor",
}

#mostrandos apenas as chaves
print(dicionario.keys())

#mostrando apenas os valores
print(dicionario.items())



#exibindo chave e valor
for chave, valor in dicionario.items():
    print(f"{chave} --- {valor}")