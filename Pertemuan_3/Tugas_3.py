#Penjumlahan Matriks
matriks_1 = [
    [2, 5],
    [1, 4],
]

matriks_2 = [
    [2, 4],
    [8, 2],
]
for x in range(0, len(matriks_1)):
    for y in range(0, len(matriks_2[0])):
        print (matriks_1[x][y] + matriks_2[x][y], end=' '),
    print