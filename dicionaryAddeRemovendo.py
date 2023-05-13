dicionario= {
    "chave_valor":  "result",  #chave_valor armazena o conteudo "result"
    "linguagem":  "c#",
    "sonho":  "desenvolvedor",
}


#add valor

dicionario["Viajem"] = "Bahamas"
print(dicionario.values())

#alterando dados
dicionario["Viajem"] = "Paris" #agr a chave viagem vai receber Paris

#user add valores

nome_colaborador = input("Informe o nome do colaborador: ")

cargo_colaborador = input("Informe o cargo do colaborador {}: ".format(nome_colaborador))

dicionario[nome_colaborador] = cargo_colaborador

for chave, valor in dicionario.items():
    print(F"{chave} ----- {valor}")
    
    
    
#removendo valores
#pop(chave) -- remove tanto a chave e o valor junto daquele dicionary

dicionario.pop("Viajem") #removem a chave viajem e o valor Paris

print("========================")
for chave, valor in dicionario.items():
    print(F"{chave} ----- {valor}")
    
#popitem
#o popitem remove o ultimo elemento do meu dicionary automaticamente, sem necessitar passar um parametro

dicionario.popitem() #ultimo elemento é Leandro --- dev, entao foi removido

print("--------------------")
for chave, valor in dicionario.items():
    print(F"{chave} ---- {valor}")