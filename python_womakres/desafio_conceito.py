nome = input("Qual o seu nome? ")
# inserido o int para converter idade para numero inteiro
idade = int(input("Qual a sua idade? "))
# inserido o float para converter altura em numero flutuante 
altura = float(input("Qual a sua altura? "))
# inserido o int para converter ano atual para numero inteiro
ano_atual = int(input("Qual ano você nasceu? "))

# saber ano de nascimento 
linha_tempo1 = 2025 - idade
# saber qual a idade para daqui a 5 anos 
linha_tempo2 = idade + 5

#saber o dobro da idade da pessoa
especial_dobro = idade * 2
# saber a idade elevada ao quadrado
especial_quadrado = idade ** 2


print("Olá", nome)
print("Seja bem vindo(a)")
print("Sua idade é: ", idade )
print("Sua altura é: ", altura )
print("Sua Você nasceu no ano: ", linha_tempo1 )
print("Daqui a 5 anos você terá: ", linha_tempo2 )
print("O dobro da sua idade é: ", especial_dobro )
print("Sua idade ao quadrado é: ", especial_quadrado )
# saber se é maior de 18 anos 
print (idade >= 18)
# saber se tem mais de 1.60 de altura
print (altura >= 1.60)