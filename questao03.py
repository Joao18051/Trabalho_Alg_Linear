import numpy as np

matriz = []
matriz_inv = []
matriz_cof = []

def det(matriz, tamanho):
    determinante = 0

    if (tamanho >= 3):
        for quant_de_matriz in range(0, tamanho):
            recorrencia = []

            for i in range(0, tamanho):
                recorrencia.append(matriz[i])
                    
            recorrencia = np.delete(recorrencia, (quant_de_matriz), axis=0) #apaga linha
            recorrencia = np.delete(recorrencia, (0), axis=1) #apaga coluna

            valor = det(recorrencia, tamanho -1)

            determinante += ((-1) **(quant_de_matriz +2)) *matriz[quant_de_matriz][0] *valor
    
    elif (tamanho == 2):
        determinante += matriz [0][0] *matriz[1][1]
        determinante -= matriz [0][1] *matriz[1][0]
    
    elif (tamanho == 1):
        determinante = matriz [0][0]
    
    return determinante

def cofa(matriz, tamanho):
    for l in range(0, tamanho):
        linha = []
        for coluna in range(0, tamanho):
            recorrencia = []

            for i in range(0, tamanho):
                recorrencia.append(matriz[i])

            recorrencia = np.delete(recorrencia, (l), axis=0) #Apaga Linha
            recorrencia = np.delete(recorrencia, (coluna), axis=1) #Apaga Coluna

            determinante = det(recorrencia, tamanho -1)
            elemento = determinante *((-1) **(2 +coluna +l))

            linha.append(elemento)

        matriz_cof.append(linha)

tamanho = int(input("Informe o tamanho da matriz quadrada: "))
linha = coluna = tamanho

for l in range(0, tamanho):
    linha = []

    for coluna in range(0, tamanho):
        elemento = int(input(f"Informe o elemento na posição [{l +1}] [{coluna +1}]: "))
        linha.append(elemento)

    matriz.append(linha)

matriz = np.array(matriz)

if(det(matriz, tamanho)):

    cofa(matriz, tamanho) #cria a matriz dos cofatores

    transposta = list(zip(*matriz_cof)) #Cria a matriz transposta

    for l in range(0, tamanho):
        linha = []
        for coluna in range(0, tamanho):
            elemento = transposta[l][coluna] *(1 /det(matriz, tamanho))

            linha.append(elemento)
        matriz_inv.append(linha)

    print('A  matriz inversa é: ')
    for l in range(0, tamanho):
        for coluna in range(0, tamanho):
            print(f'[{matriz_inv [l] [coluna]:^3}]', end ='')

        print()
else:
    print(f'O determinante dessa matriz vale {det(matriz, tamanho)}, mas a inversa existe apenas para determinantes != de {det(matriz, tamanho)}')

