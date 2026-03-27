# Dicionário de dadps em python

aluna ={
    "nome": "Ana",
    "idade": 45,
    "curso": "Python",
    "status": True

}

print(aluna) # saida : 'nome': 'Ana', 'idade': 45, 'curso': 'Python', 'status': True
print(aluna["nome"]) # saida : Ana 

aluna["idade"] = 54
aluna["cidade"] = "São Paulo"

print(aluna) # saida : 'nome': 'Ana', 'idade': 45, 'curso': 'Python', 'status': True, 'cidade': 'São paulo'

aluna.pop("idade")
print(aluna) # saida : 'nome': 'Ana', 'curso': 'Python', 'status': True, 'cidade': 'São paulo'
