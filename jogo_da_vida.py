#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Estados
"" = vazio
0 = morto
1 = vivo
"""
matriz_partida = [[1, 1, 1], [1, "", ""], ['', 1, ""]]
nova_geracao = [['', '', ''], ['', '', ''], ['', '', '']]
tamanho_matriz = len(matriz_partida)

def criterio_parada(matriz):
    for i in range(len(matriz)):
        if 1 in matriz[i]:
            return True

continuar = True
k = 1

while continuar == True:
    for i in range(0, tamanho_matriz):
        for j in range(0, tamanho_matriz):
            if matriz_partida[i][j] != '':

                # elementos centrais

                if i != 0 and i != tamanho_matriz - 1 and j != 0 and j!= tamanho_matriz - 1:
                    if i == 1:
                        if matriz_partida[i][j] != '':
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
                        if (matriz_partida[i][j] == 1 and qtd_vizinhos < 2) or (matriz_partida[i][j] == 1 and qtd_vizinhos > 3):
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2 or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                # primeira linha

                if i == 0:
                    if j == 0:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i][j + 1])
                            vizinhos.append(matriz_partida[i + 1][j])
                            vizinhos.append(matriz_partida[i + 1][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2 or matriz_partida[i][j] == 1 and qtd_vizinhos > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2 or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                    if j == tamanho_matriz - 2:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i][j - 1])
                            vizinhos.append(matriz_partida[i + 1][j + 1])
                            vizinhos.append(matriz_partida[i + 1][j - 1])
                            vizinhos.append(matriz_partida[i + 1][j])
                            vizinhos.append(matriz_partida[i + 1][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2  or matriz_partida[i][j] == 1 and qtd_vizinhos  > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2 or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                    if j == tamanho_matriz - 1:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i][j - 1])
                            vizinhos.append(matriz_partida[i + 1][j - 1])
                            vizinhos.append(matriz_partida[i + 1][j])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2 or matriz_partida[i][j] == 1 and qtd_vizinhos > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2 or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                # ultima linha

                if i == tamanho_matriz - 1:
                    if j == 0:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i - 1][j])
                            vizinhos.append(matriz_partida[i - 1][j + 1])
                            vizinhos.append(matriz_partida[i][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2 or matriz_partida[i][j] == 1 and qtd_vizinhos > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2
                                or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                    if j == tamanho_matriz - 2:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i][j - 1])
                            vizinhos.append(matriz_partida[i - 1][j - 1])
                            vizinhos.append(matriz_partida[i - 1][j])
                            vizinhos.append(matriz_partida[i - 1][j + 1])
                            vizinhos.append(matriz_partida[i][j + 1])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2 or matriz_partida[i][j] == 1 and qtd_vizinhos > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2 or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                    if j == tamanho_matriz - 1:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i][j - 1])
                            vizinhos.append(matriz_partida[i - 1][j - 1])
                            vizinhos.append(matriz_partida[i - 1][j])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2 or matriz_partida[i][j] == 1 and qtd_vizinhos  > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2
                                or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                # primeira coluna

                if j == 0:
                    if i == 1:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i - 1][j])
                            vizinhos.append(matriz_partida[i - 1][j + 1])
                            vizinhos.append(matriz_partida[i][j + 1])
                            vizinhos.append(matriz_partida[i + 1][j + 1])
                            vizinhos.append(matriz_partida[i + 1][j])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2  or matriz_partida[i][j] == 1 and qtd_vizinhos  > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2 or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1

                # ultima coluna

                if j == tamanho_matriz - 1:
                    if i == 1:
                        if matriz_partida[i][j] != '':
                            vizinhos = []
                            vizinhos.append(matriz_partida[i - 1][j])
                            vizinhos.append(matriz_partida[i - 1][j - 1])
                            vizinhos.append(matriz_partida[i][j - 1])
                            vizinhos.append(matriz_partida[i + 1][j - 1])
                            vizinhos.append(matriz_partida[i + 1][j])
                        qtd_vizinhos = vizinhos.count(1)
                        if matriz_partida[i][j] == 1 and qtd_vizinhos < 2 or matriz_partida[i][j] == 1 and qtd_vizinhos > 3:
                            nova_geracao[i][j] = 0
                        if matriz_partida[i][j] == 0 and qtd_vizinhos == 3:
                            nova_geracao[i][j] = 1
                        if matriz_partida[i][j] == 1 and (qtd_vizinhos == 2 or qtd_vizinhos == 3):
                            nova_geracao[i][j] = 1
            else:
                nova_geracao[i][j] == ''

    if k - 1 == 0:
        print(f'1ª geração: {matriz_partida}')
    del matriz_partida[:]
    matriz_partida = nova_geracao.copy()
    print(f'{k+1}ª geração: {nova_geracao}')
    continuar = criterio_parada(matriz_partida)
    if k > 98:
        continuar = False
    k += 1
