# manipulação de arquivo

import os
arquivo = "aluna.txt"
alunas = []

# cria um arquivo com a lista de nomes informadas 
#with open(arquivo, mode="w", encoding="utf-8") as lista:
#    lista.write("Ana\n")
#    lista.write("Beatriz\n")
#    lista.write("Gisele\n")
############################################################

# cria espaço de leitura no final da lista 
#with open(arquivo, mode="r", encoding="utf-8") as lista:
#    conteudo = lista.read()  

# print(conteudo)
 ##############################################################

# imprime a lista organizada e limpa sem espaços ou quebra de linha com strip   
#with open(arquivo, mode="r", encoding="utf-8") as lista:
#    for linha in lista:
#        print(linha.strip()) 

######################################################################

# imprime a lista inclusive \n colocado para espaçar os nomes 
#with open(arquivo, mode="r", encoding="utf-8") as lista:
#    linhas = lista.readlines()
#print(linhas) 

######################################################################

# inserir laço de repetição para que os nomes saia em uma Lista
#with open(arquivo, mode="r", encoding="utf-8") as lista:
#    for linhas in lista.readlines():
#        alunas.append(linhas.strip())
#print(alunas) # saida ['Ana', 'Beatriz', 'Gisele']

######################################################################

# alterar conteudo do nosso arquivo 

# para apagar um nome da lista dentro do arquivo
# a letra "r" é de readlines
#with open(arquivo, mode="r", encoding="utf-8") as lista:
#    alunas = lista.readlines()

#alunas_atualizadas = []

# strip remove linhas em branco
#for aluna in alunas:
#    nome  = aluna.strip()

# o nome Gisele vai ser retirado na lista, pois esta reescrendo os nome que são diferentes de Gisele
#    if nome != "Gisele":
#        alunas_atualizadas.append(nome)

# a letra "W" é de Write 
#with open(arquivo, mode="w", encoding="utf-8") as lista:
#    for aluna in alunas_atualizadas:
#        lista.write(aluna + "\n")

#adicionando um nome a lista
# a letra "a" é de append, para adicionar 
#with open(arquivo, mode="a", encoding="utf-8") as lista:
#    lista.write("Daniela\n")


###############################################################

# deletar arquivo

if os.path.exists(arquivo):
    os.remove(arquivo)
    print("Arquivo removido")
else:
    print("Arquivo não encontrado")

