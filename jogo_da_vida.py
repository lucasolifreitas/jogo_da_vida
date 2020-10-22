#!/usr/bin/python
# -*- coding: utf-8 -*-

import copy

"""
Estados
0 = morto
1 = vivo

A entrada do script é uma matriz contendo apenas 0 e 1, indicando o estado da célula.
A "matriz_partida" representa a matriz inicial, ou seja, a 1ª geração.
Logo abaixo tem alguns exemplos de matrizes de entrada.
"""

#exemplos de entradas

matriz_partida = [[0,1,1,0],[1,1,1,0],[0,1,0,1],[0,0,1,1]]
#matriz_partida = [[1,1,1],[0,0,1],[0,1,0]]
#matriz_partida = [[0, 1,1,1], [1,1,1,0]]
#matriz_partida = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
#matriz_partida = [[0,1,0,0,1], [1,0,0,0,0], [1, 0, 0,0, 1], [1,1,1,1,0]]
#matriz_partida = [[1,0,1,3],[1,0,0,1],[1,0,0,1],[0,0,1,1]]
#matriz_partida = [[0, 1, 0, 0], [1, 0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 1]]
#matriz_partida = [[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 1]]
#matriz_partida = [[1,0], [0, 1]]
#matriz_partida = [[0,0]]

tamanho_matriz = len(matriz_partida)
tamanho_matriz_col = len(matriz_partida[0])


#codígo para criar uma matriz de zeros que será atualizada de acordo com as iterações do jogo
nova_geracao = []
linha = []
nc = tamanho_matriz_col
nl = tamanho_matriz
for c1 in range(0, nl):
    linha = []
    for c2 in range(0, nc):
        n = 0
        linha.append(n)
    nova_geracao.append(linha)

b = copy.deepcopy(nova_geracao)

#verifica se na matriz partida so contem 1 ou 0, que indica o estado da celula
def verifica_matriz(matriz):
    for a in range(len(matriz)):
        for b in range(len(matriz[a])):
            if not (matriz[a][b] == 1 or matriz[a][b] == 0):
                del matriz[:]
                matriz = -1
                return matriz
        return matriz


#Enquanto alguma célula for do estado "viva"
def criterio_parada(matriz):
    for i in range(len(matriz)):
        if 1 in matriz[i]:
            return True

#Regras estabelecidas do jogo da vida
def regras_jogo_vida(matriz, qtd_vizinhos):
    if matriz_partida[i][j] == 1:
        if qtd_vizinhos < 2 or qtd_vizinhos > 3:
            nova_geracao[i][j] = 0
        if qtd_vizinhos == 2 or qtd_vizinhos == 3:
            nova_geracao[i][j] = 1
    else:
        if qtd_vizinhos == 3:
            nova_geracao[i][j] = 1

    return nova_geracao


verifica_matriz(matriz_partida)

#scrip principal do jogo

try:

    continuar = True
    k = 1

    while continuar == True:
        for i in range(0, tamanho_matriz):
            for j in range(0, tamanho_matriz_col):
                # elementos centrais
                if (i != 0) and (i != tamanho_matriz - 1) and (j != 0) and (j!= tamanho_matriz_col - 1):
                    vizinhos = []
                    vizinhos.append(matriz_partida[i - 1][j])
                    vizinhos.append(matriz_partida[i - 1][j - 1])
                    vizinhos.append(matriz_partida[i][j - 1])
                    vizinhos.append(matriz_partida[i + 1][j - 1])
                    vizinhos.append(matriz_partida[i + 1][j])
                    vizinhos.append(matriz_partida[i - 1][j + 1])
                    vizinhos.append(matriz_partida[i][j + 1])
                    vizinhos.append(matriz_partida[i + 1][j + 1])
                    qtd_vizinhos = vizinhos.count(1)
                    nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                # primeira linha
                if i == 0:
                    if j == 0:
                        vizinhos = []
                        vizinhos.append(matriz_partida[i][j + 1])
                        vizinhos.append(matriz_partida[i + 1][j])
                        vizinhos.append(matriz_partida[i + 1][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                    elif j == tamanho_matriz_col - 1:
                        vizinhos = []
                        vizinhos.append(matriz_partida[i][j - 1])
                        vizinhos.append(matriz_partida[i + 1][j - 1])
                        vizinhos.append(matriz_partida[i + 1][j])
                        qtd_vizinhos = vizinhos.count(1)
                        nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                    else:
                        vizinhos = []
                        vizinhos.append(matriz_partida[i][j - 1])
                        vizinhos.append(matriz_partida[i + 1][j + 1])
                        vizinhos.append(matriz_partida[i + 1][j - 1])
                        vizinhos.append(matriz_partida[i + 1][j])
                        vizinhos.append(matriz_partida[i][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                # ultima linha
                if i == tamanho_matriz - 1:
                    if j == 0:
                        vizinhos = []
                        vizinhos.append(matriz_partida[i - 1][j])
                        vizinhos.append(matriz_partida[i - 1][j + 1])
                        vizinhos.append(matriz_partida[i][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                    elif j == tamanho_matriz_col - 1:
                        vizinhos = []
                        vizinhos.append(matriz_partida[i][j - 1])
                        vizinhos.append(matriz_partida[i - 1][j - 1])
                        vizinhos.append(matriz_partida[i - 1][j])
                        qtd_vizinhos = vizinhos.count(1)
                        nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                    else:
                        vizinhos = []
                        vizinhos.append(matriz_partida[i][j - 1])
                        vizinhos.append(matriz_partida[i - 1][j - 1])
                        vizinhos.append(matriz_partida[i - 1][j])
                        vizinhos.append(matriz_partida[i - 1][j + 1])
                        vizinhos.append(matriz_partida[i][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                # primeira coluna
                if (j == 0) and (i!=0) and (i!=tamanho_matriz-1):
                    vizinhos = []
                    vizinhos.append(matriz_partida[i - 1][j])
                    vizinhos.append(matriz_partida[i - 1][j + 1])
                    vizinhos.append(matriz_partida[i][j + 1])
                    vizinhos.append(matriz_partida[i + 1][j + 1])
                    vizinhos.append(matriz_partida[i + 1][j])
                    qtd_vizinhos = vizinhos.count(1)
                    nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

                # ultima coluna
                if (j == tamanho_matriz_col - 1) and (i!=0) and (i!=tamanho_matriz-1):
                    vizinhos = []
                    vizinhos.append(matriz_partida[i - 1][j])
                    vizinhos.append(matriz_partida[i - 1][j - 1])
                    vizinhos.append(matriz_partida[i][j - 1])
                    vizinhos.append(matriz_partida[i + 1][j - 1])
                    vizinhos.append(matriz_partida[i + 1][j])
                    qtd_vizinhos = vizinhos.count(1)
                    nova_geracao = regras_jogo_vida(matriz_partida, qtd_vizinhos)

        if k - 1 == 0:

            print(f'1ª geração: {matriz_partida}')
            for linha in matriz_partida:
                for numero in linha:
                    print(f'{numero:>3}', end=" ")
                print()
            print('------------------------------\n')

        #para a proxima iteração a matriz_partida passa ser a matriz nova_geração gerada anteriormente
        del matriz_partida[:]
        matriz_partida = copy.deepcopy(nova_geracao)

        print(f'{k+1}ª geração: {nova_geracao}')
        for linha in nova_geracao:
            for numero in linha:
                print(f'{numero:>3}', end=" ")
            print()
        print('------------------------------\n')

        del nova_geracao[:]
        nova_geracao = copy.deepcopy(b)

        continuar = criterio_parada(matriz_partida)
        #Como tem entradas que geram iterações infinitas estipulei para esse script o máximo de 100 gerações
        if k > 98:
            continuar = False
        k += 1
except IndexError:
    print('A "matriz partida" deve ser no mínimo uma matriz 2x2.\n'
          'Vale ressaltar que todos campos da matriz devem ser preenchidos\n'
          'somente com 1 ou 0, onde 1 representa o estado VIVO e 0 o estado MORTO!')







