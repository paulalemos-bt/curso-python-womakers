# funcoes

def saudacao(nome, estado):
    print(f"{nome}, Seja bem vinda. Muito bom ver alguem de {estado}")

#saudacao("Ana", "PE") #saida: Ana seja bem vinda. Muito bom ver alguem de PE



def soma(a, b):
    return a + b

resultado = soma(5,3)
# print(resultado) # saida: 8

def verificar_idade(idade):
    if idade >= 18:
        return " Maior de idade"
    else:
        return"Menor de idade"
    
print(verificar_idade(16))