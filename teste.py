arquivo = open ("interpreterworkflow.wk","r")  #(endereço,modo)  r = ler
conteudo= arquivo.read()   #funcao para retornar conteudo do arquivo retornando string
arquivo.close()            #funcao para liberar recrusos

print(conteudo)


#arquivo = open ("mensagem.txt","w")  w = escrever , notar que se o arquivo ja existir ele ira deletar e escrever
#conteudo = arquivo.write()
arquivo.close()