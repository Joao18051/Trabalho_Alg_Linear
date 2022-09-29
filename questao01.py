import numpy as np

matriz = []
determinante = 0

def det(matriz, tamanho):
    determinante = 0

    if (tamanho >= 3):
        for quant_de_matriz in range(0, tamanho):
            recorrencia = []
            recorrencia.clear()

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

tamanho = int(input(print("Informe o tamanho da matriz quadrada: ")))
linha = coluna = tamanho

for l in range(0, tamanho):
    linha = []

    for coluna in range(0, tamanho):
        elemento = int(input(f"Informe o elemento na posição [{l +1}] [{coluna +1}]: "))
        linha.append(elemento)

    matriz.append(linha)

matriz = np.array(matriz)

for linha in range(0, tamanho):
    for coluna in range(0, tamanho):
        print(f'[{matriz [linha] [coluna]:^3}]', end ='')

    print()

print(f'O determinante dessa matriz vale: {det(matriz, tamanho)}')
            