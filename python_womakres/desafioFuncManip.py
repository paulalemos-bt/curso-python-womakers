
# SISTEMA: MEMÓRIA MULHERES TECH

# nome do arquivo onde os dados serão salvos
ARQUIVO = "memoria_mulheres_tech.txt"

# lista em memória (estrutura de dados)
mulheres = []


# função para salvar o arquivo
def salvar_no_arquivo(registro):
    try:
        with open(ARQUIVO, "a", encoding="utf-8") as arquivo:
            # salvando de forma organizada
            arquivo.write(f"nome:{registro['nome']}\n")
            arquivo.write(f"area:{registro['area']}\n")
            arquivo.write(f"contribuicao:{registro['contribuicao']}\n")
            arquivo.write(f"ano:{registro['ano']}\n")
            arquivo.write("---\n")
    except Exception as e:
        print("Erro ao salvar no arquivo:", e)



# função para ler o arquivo
def ler_arquivo():
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return arquivo.readlines()
    except FileNotFoundError:
        print("Nenhum registro encontrado ainda.")
        return []
    except Exception as e:
        print("Erro ao ler arquivo:", e)
        return []



# MENU INTERATIVO (WHILE)

opcao = 0

while opcao != 5:
    print("\n=== MEMÓRIA MULHERES TECH ===")
    print("1. Cadastrar mulher tech")
    print("2. Listar histórico")
    print("3. Buscar por nome")
    print("4. Exibir estatísticas")
    print("5. Sair")

    # tratamento de erro para entrada inválida
    try:
        opcao = int(input("Escolha uma opção: "))
    except:
        print("Digite um número válido!")
        continue

    
    # OPÇÃO 1 - CADASTRO
    
    if opcao == 1:
        nome = input("Nome: ")
        area = input("Área de atuação: ")
        contribuicao = input("Contribuição: ")

        # tratamento para ano inválido
        try:
            ano = int(input("Ano ou período: "))
        except:
            print("Ano inválido! Digite apenas números.")
            continue

        # criação do dicionário (estrutura de dados)
        registro = {
            "nome": nome,
            "area": area,
            "contribuicao": contribuicao,
            "ano": ano
        }

        mulheres.append(registro)  # adiciona na lista

        salvar_no_arquivo(registro)  # salva no arquivo

        print("Cadastro realizado com sucesso!")

    
    # OPÇÃO 2 - LISTAR HISTÓRICO
    
    elif opcao == 2:
        linhas = ler_arquivo()

        print("\n--- Mulheres que Transformaram a Tecnologia ---")

        registro = {}

        for linha in linhas:
            linha = linha.strip()

            if linha == "---":
                print(f"Nome: {registro.get('nome', '')}")
                print(f"Área: {registro.get('area', '')}")
                print(f"Contribuição: {registro.get('contribuicao', '')}")
                print(f"Ano: {registro.get('ano', '')}")
                print("-" * 50)
                registro = {}
            else:
                try:
                    chave, valor = linha.split(":", 1)
                    registro[chave] = valor
                except:
                    pass

    
    # OPÇÃO 3 - BUSCAR POR NOME
    
    elif opcao == 3:
        busca = input("Digite o nome para busca: ").lower()

        linhas = ler_arquivo()

        registro = {}
        encontrado = False

        for linha in linhas:
            linha = linha.strip()

            if linha == "---":
                if "nome" in registro and busca in registro["nome"].lower():
                    print("\nEncontrado:")
                    print(f"Nome: {registro.get('nome', '')}")
                    print(f"Área: {registro.get('area', '')}")
                    print(f"Contribuição: {registro.get('contribuicao', '')}")
                    print(f"Ano: {registro.get('ano', '')}")
                    print("-" * 50)
                    encontrado = True
                registro = {}
            else:
                try:
                    chave, valor = linha.split(":", 1)
                    registro[chave] = valor
                except:
                    pass

        if not encontrado:
            print("Nenhum resultado encontrado.")

    
    # OPÇÃO 4 - ESTATÍSTICAS
    
    elif opcao == 4:
        linhas = ler_arquivo()

        anos = []
        total = 0
        registro = {}

        for linha in linhas:
            linha = linha.strip()

            if linha == "---":
                if "ano" in registro:
                    try:
                        anos.append(int(registro["ano"]))
                        total += 1
                    except:
                        pass
                registro = {}
            else:
                try:
                    chave, valor = linha.split(":", 1)
                    registro[chave] = valor
                except:
                    pass

        if total == 0:
            print("Nenhum dado disponível.")
        else:
            print("Total cadastradas:", total)
            print("Ano mais antigo:", min(anos))
            print("Ano mais recente:", max(anos))

    
    # OPÇÃO 5 - SAIR
    
    elif opcao == 5:
        print("\nEste arquivo existe porque histórias importam.")
        print("Mulheres sempre estiveram presentes na tecnologia.")
        print("E agora, você também faz parte dessa transformação ❤️")

    else:
        print("Opção inválida!")