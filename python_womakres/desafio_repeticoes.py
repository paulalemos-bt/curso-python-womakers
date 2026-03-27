
valorA = int(input("Qual é o valor A? "))
valorB = int(input("Qual é o valor B? "))

Resultado_soma = valorA + valorB
contador = 0

if Resultado_soma >= 10:
    # colocou o round para poder arredonar o valor para no máximo duas casas decimais 
    print ("valor menor que 10: ", round(Resultado_soma, 2))

else:
    print ("Valor menor que 10: ", round(Resultado_soma, 2))         


while contador<3:
    contador +=1
    print ("Você conseguiu")



