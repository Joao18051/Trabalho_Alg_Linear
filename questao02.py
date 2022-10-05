from numpy.linalg import solve

matriz_direitos = []
matriz_esquerdos = []

base_1 = [] #Cada linha representa um vetor diferente da base e cada coluna um elemento diferente
base_2 = []

def calcularSistemaLinearRn(valores_esquerdos, valores_direitos):
    a = [valores_esquerdos]
    b = [valores_direitos]

    return solve(a, b)

Rn = int(input("Informe o n de Rn: "))

for j in range(0, Rn): #Cria a base, cada linha é um vetor diferente
    linha = []
    for i in range(0, Rn):
        li = int(input(f"Informe o [{i +1}] elemento do [{j +1}] vetor da Base inicial para conversão: "))
            
        linha.append(li)
    base_1.append(linha)

    linha = []
    for i in range(0, Rn): #Cria a base, cada linha é um vetor diferente
        lf = int(input(f"Informe o [{i +1}] elemento do [{j +1}] vetor da Base final para conversão: "))
        linha.append(lf)
    base_2.append(linha)

if Rn == 1:
    print(calcularSistemaLinearRn(base_1[0], base_2[0]))

else:
    for abscissa in range(0, Rn):
        a = []

        for coluna in range(0, Rn):
            elemento = base_1[abscissa][coluna]
            a.append(elemento)
        matriz_direitos.append(a)
    
    for abscissa in range(0, Rn):
        x = []

        for coluna in range(0, Rn):
            elemento = base_2[abscissa][coluna]
            x.append(elemento)
        matriz_esquerdos.append(x)

    for i in range(0, Rn):
            print(calcularSistemaLinearRn(matriz_esquerdos, matriz_direitos[i]))