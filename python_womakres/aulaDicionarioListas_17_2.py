# Dicionário e listas de dados em python

escola = [
    {
    "nome": "Ana",
    "idade": 45,
    "curso": "Python",
    "status": True

     },
     {
    "nome": "Cynthia",
    "idade": 34,
    "curso": "C#",
    "status": True

     },
     {
    "nome": "Clarice",
    "idade": 24,
    "curso": "Dados",
    "status": False

     }


]

# a impressão é efetuada de todas as alunas juntas em uma unida linha,
# as informações ficam misturadas e sem organização
#print(escola)

# colocando o for a impressão fica organizada, e cada aluna em uma linha
# 'nome': 'Ana', 'idade': 45, 'curso': 'Python', 'status': True
# 'nome': 'Cybthia', 'idade': 34, 'curso': 'C#', 'status': True
# 'nome': 'Clarice', 'idade': 24, 'curso': 'Dados', 'status': False

#for aluna   in escola:
#    print(aluna)



###################################################################################

#for aluna   in escola:
#    print(f"Nome: {aluna['nome']}")
#    print(f"curso: {aluna['curso']}")
#    print("-" * 20)
    
# a saida vai ser :
#Nome: Ana
#curso: Python       
#--------------------
#Nome: Cybthia       
#curso: C#
#--------------------
#Nome: Clarice       
#curso: Dados        
#--------------------


###########################################################

#nome_da_escola = "WoMakers"

#print(f"Escola: {nome_da_escola}") # saida Escola: WoMakers

######################################################

#aluna = escola[2]
#print(aluna) # saida nome': 'Clarice', 'idade': 24, 'curso': 'Dados', 'status': False

##########################################################

for aluna   in escola:
    if aluna["nome"] == "Cynthia":
           print(f"Nome: {aluna['nome']}")
           print(f"Curso: {aluna['curso']}")









