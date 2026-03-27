#Repetindo tarefas com FOR

#n = 4


#for i in range(0, n):
    #print(i) ### saida 0,1,2,3

############################################

#nome = "Ana"

#for letra in nome:
#    print(letra) # saida a, n ,a

#############################################

#tecnologias = ["Python", "dados", "IA"]
#for item in tecnologias:
#   print(item) # saida Python, dados, IA

############################################

#tecnologias = ["Python", "dados", "IA"]
#perfil = {"nome": "Ana", "estado": "RS"}
#for chave in perfil:
#    print(chave, perfil[chave]) # saida nome Ana
                                 #      estadp RS

############################################
                                 
#tecnologias = ["Python", "dados", "IA"]

#for item in range(len(tecnologias)):
    #print(tecnologias[item]) # saida   Python, Dados, IA    

###################################################   

# indica quantas vezes quero que repita a frase 
# e com o indice faz a contagem de quantas vezes foram feitas
#for indice in range(5):
   # print("Repetindo!", indice)
   # print("Oie, WoMakers!") # saida: repetindo!0, Oie, WoMakers


###################################################

indice = 0

for item in range(3):
    indice += item 
    print("Numero atual", indice)
                          

