# utilizando tupla
Curso_Python = ("Python para Iniciantes", 3, 60)
# nome do curso:
# duração (em meses)
# carga hoária total (em horas)

# tuplas são valores que não podem ser alterados 

print("Nome do curso:", Curso_Python[0]) # saida Python para Iniciantes
print("Duração (meses):", Curso_Python[1]) # 3
print("Carga horária (horas):", Curso_Python[2]) # 60

# criando um diocionário e uma lista 
participantes = []

opcao = 0

#criando um menu com while
while opcao != 4:
    print("\n === Menu ===")
    print("1. Cadastrar participante")
    print("2. Mostrar participante")
    print("3. Mostrar Análises")
    print("4. Sair")

    opcao = int(input("Escolha uma opção "))

# cadastro do partipante 
    if opcao == 1:
        nome = input("Digite o nome do participarnte: ")
        idade = int(input("Digite sua idade: "))
        horas = float(input("Quanta horas de estudo: "))
        area = input("Digite sua área de interesse: ")

        # validação
        if idade < 0 or horas < 0:
            print("Idade ou horas não podem ser negativas")
            continue  # estrutura de controle 
        
        # condicionais 
        # operações de comparação
        maior_idade = idade >= 18
        meta_estudo = horas >= 5 

        # operações matemáticas 
        dobro_idade = idade * 2
        idade_quadrado = idade **2

        # dicionário
        participante = {
            "nome": nome,
            "idade": idade,
            "horas_estudo": horas,
            "area_interesse": area,
            "maior_idade": maior_idade,
            "meta_estudo": meta_estudo,
            "dobro_idade": dobro_idade,
            "idade_quadrado": idade_quadrado

        }
        
        # adionando participantes a lista 
        participantes.append(participante)
        print("Participante cadastrado com sucesso!")
    
    # mostrar os participantes 
    elif opcao == 2:
        print("\n ====== LISTA DE PARTICIPANTES ====== ")

        if len(participantes) == 0:
            print ("Nenhum participante Cadastrado.")
        else:

            for p in participantes:   # estrutura de controle for
                print("\n ====== PARTICIPANTE ======")
                print("Nome:", p["nome"])
                print("Idade:", p["idade"])
                print("Horas de estudo:", p["horas_estudo"])
                print("Àrea de interesse:", p["area_interesse"])

                #resultado das condicionais 
                print("Maior de Idade:", p["maior_idade"])
                print("Cumpre meta de estudo:", p["meta_estudo"])

                # resultado matematicos
                print("Dobro da idade:", p["dobro_idade"])
                print("Idade ao quadrado", p["idade_quadrado"])

   #analises de for 
    elif opcao == 3:
        print("\n =====  ANÁLISES  =====")
        total = len(participantes)

        if total == 0:
            print(" Nenhum dado para análise.")

        else:
            soma_horas = 0
            acima_meta = []
            areas = set()     # não repete valores

            for p in participantes:         # estrutura de controle (for)
                soma_horas += p["horas_estudo"]

                if p["meta_estudo"]:   ## codicional
                    acima_meta.append(p["nome"])

                areas.add(p["area_interesse"])

            media = soma_horas / total #operação matematica 

            print(" Total de participantes", total)
            print("Média de horas de estudo", media)

            print("\n ###   Alunas Acima da Meta   ###")
            for nome in acima_meta:
                print("-", nome)

            print("\n Áreas de interesse não esta repetida:")
            for area in areas:
                print("-", area)

    elif opcao == 4:
        print("Saindo do programa ...")

    else:
        print("===============")
        print("Opção inválida")
       
