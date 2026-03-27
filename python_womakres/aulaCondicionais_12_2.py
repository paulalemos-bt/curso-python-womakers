# Condiçoes com if, else e elif em python

nota1 = 7
nota2 = 9
nota3 = 5

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    # colocou o round para poder arredonar o valor para no máximo duas casas decimais 
    print ("Aprovada - nota: ", round(media, 2))
elif media >= 5:
    print ("Recuperação!: ", round(media, 2))
else:
    print ("Reprovada - nota: ", round(media, 2))         