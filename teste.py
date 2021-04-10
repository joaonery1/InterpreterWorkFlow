
import re
import string


b = "[]"
lista = []
final = ''
with open('interpreterworkflow.wk') as arquivo:
    dados = arquivo.readlines()[57:62]  # array de strings
    # print(dados)
    texto = dados  # varíavel para armazenar o array de string
    for letra in texto:  # for para transformar em string
        # print(letra)
        filtro = re.compile('([0-9]+)')  # pegar só digitos númericos
        
        resp = filtro.findall(letra)  # funcao para trasnformar em números
        #resp = list(map(int, resp))  # função apra transformar em inteiros
        print(resp)

       # print(resp)
        for ares in resp:
            resp = list(map(int, resp))
            lista.append(ares)
#print(lista)       


'''
    filtro =  re.compile('([0-9]+)')
    resp = filtro.findall(texto)
    print(resp)   
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
'''
