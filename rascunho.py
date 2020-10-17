a = [[0, 0, 0], ['', 0, 0], ['', '', 0]]

def criterio_parada(matriz):
    for i in range(len(matriz)):
        if 1 in a[i]:
            return True


print(criterio_parada(a))

if criterio_parada(a) == True:
    print('ok')
else:
    print('nao ok')