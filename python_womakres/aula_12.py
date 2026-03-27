# Condições com if, else e elif em python

idade = 60
e_membro = False

if idade >= 60:
    if e_membro:
        print("30% de desconcto")
    else:
        print("20% de desconto") 
elif idade >= 50:
    print("Vale compras com cashback")
else:
    print("sem desconto!")             
