#!/usr/bin/env python3



nome = "interpreterworkflow.wk"

with open(nome, "r") as arquivo:  # (endereço,modo)  r = ler
    for linha in arquivo:
        linha = arquivo.readlines()
        for linha in linha:
            linha_sem = linha.split()
            for linha_sem in linha_sem:
                palavra = linha_sem.split()
                print(palavra)
    

  
    

# arquivo = open ("mensagem.txt","w")  w = escrever , notar que se o arquivo ja existir ele ira deletar e escrever
# conteudo = arquivo.write()
    # arquivo.close()
