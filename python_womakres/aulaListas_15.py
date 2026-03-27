# Listas em Python

cursos = ["Python", "Git", "Designe", "CV"]

# imprimindo alista e o indice 1
print(cursos) # sada: Python , Git, designe, CV
print(cursos[1]) # saida: Python

#alterando o indice 1
cursos[1] = "Git e GitHub"
print(cursos) # sada: Python , Git e GitHub, designe, CV

# Adicionando um valor 
cursos.append("Dados")
print(cursos) # sada: Python , Git e GitHub, designe, CV

# Removendo 2 cursos
cursos.remove("Designe")
cursos.pop(0)
print(cursos) # sada: Git e GitHub, CV, DAdos
