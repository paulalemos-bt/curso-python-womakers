# tratamento de erros 

# try significa tentar executa nosso bloco de codigo

#try:
#    numero = int(input("Digite um número: "))
#    print(10/ numero)
#    # por exemplo se voc^digitar no imput a palavra "testo"
#    # vai sar a resposta "Ocorreu um erro"
#except:
#    print("Ocorreu um erro")

####################################################################

#try:
#    numero = int(input("Digite um número: "))
#    resultado = 10 / numero
#
#    # o except já tem alguma exessoes pre definidas


# se digitar ZERO vai aparecer a informação    
#except ZeroDivisionError:
#    print("Não é possìvel dividir por ZERO!")

# se digitar texto vai aparecer a informação
#except ValueError:
#    print("Digite somente números")

###################################################################

try:
    arquivo = open("dados.txt", mode="r")
    conteudo = arquivo.read()

except FileNotFoundError:
    print("Arquivo não encontrado")

finally:
    print("Operação finalizada")
