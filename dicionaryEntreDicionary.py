##Add dicionarios dentre de dicionarios

contatos = {
    "Leandro Moura":{
        "Celular": "119585803670",
        "email": "leofcb334@gmail.com",
        
    },
    "Bruce Wayne":{
        "celular":  "47785666",
        "email": "batcaverna@gmail.com"
    }
      
}

print(contatos.values()) #return chave celular, email e seus atributos [{'Celular': '119585803670', 'email': 'leofcb334@gmail.com'}
print(contatos.items()) #return chavel Nome (Leandro e Bruce), celular, email e seus atributos [('Leandro Moura', {'Celular': '119585803670', 'email': 'leofcb334@gmail.com'})


print("\n\n")

#percorrendo contatos

for nome, formas_contato in contatos.items():
    print("O contato {}".format(nome))
    for tipo_contato, valor_contato in formas_contato.items():
        print("Pode ser contatado por")
        print(f"{tipo_contato} ------ {valor_contato}")
    print("\n\n")