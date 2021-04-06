def pesquisar_nodes (arq, txt):
    nome = ""
    with open ( arq , 'r') as a:
        for linha in a:
            linha = linha.strip('\n')
            if nome == "":
                if txt in linha:
                    nome = linha
            else:
                registro = linha.split(',')
                dic = {"Node" : nome
                        
                   }
            
                return dic;
    return None;

texto = pesquisar_nodes ('interpreterworkflow.wk','NodeConnection')
print(texto)



            



'''
nome = "interpreterworkflow.wk"
with open(nome, "r") as arquivo:  # (endereço,modo)  r = ler
    for linha in arquivo:
        linha = arquivo.readlines()
        for linha in linha:
            linha_sem = linha.split()
            for linha_sem in linha_sem:
                palavra = linha_sem.split()
                print(palavra)
'''

                
            
             
