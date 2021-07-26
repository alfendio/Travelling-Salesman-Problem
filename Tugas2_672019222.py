from sys import maxsize
from itertools import permutations

matriks = [ 
    [0, 5, 9, 14, 16, 11, 21],
    [5, 0, 17, 18, 12, 13, 8],
    [9, 16, 0, 6, 23, 28, 20],
    [14, 18, 6, 0, 31, 40, 37],
    [16, 12, 23, 31, 0, 33, 19],
    [11, 13, 28, 40, 33, 0, 4],
    [21, 8, 20, 37, 19, 4, 0],
]

totalKota = len(matriks)

def jalanJalan(matr, awal):
    jalanIndex = []
    for i in range(totalKota):
        if i != awal:
            jalanIndex.append(i)
    minJarak = maxsize
    maxJarak = 0
    ru = []
    rut = []
    kunjungann = []
    kunjungan = permutations(jalanIndex)
    for i in kunjungan:
        totalJarak = 0
        kotaSaatIni = awal
        for x in i:
            totalJarak += matr[kotaSaatIni][x]
            kotaSaatIni = x
        totalJarak += matr[kotaSaatIni][awal]
        if maxJarak < totalJarak:
            ru_pendek = [i,totalJarak]
            maxJarak = totalJarak
        elif minJarak > totalJarak:
            rut_panjang = [i, totalJarak]
            minJarak = totalJarak
        kunjungann.append([i, totalJarak])

        tengah = int(len(kunjungann) / 2)
        kunjungann.sort()
        rute_tengah = list(kunjungann[tengah][0])
        mid = int(kunjungann[tengah][1])
 
    #print('Rute tercepat adalah = {}'.format(list(rut_panjang[0])) % (minJarak) ('dengan total jarak adalah %d km'))
    print('a. Rute tercepat (%d km) adalah {}'.format(list(rut_panjang[0])) % (minJarak)) 
    print('b. Rute terpanjang (%d km) adalah {}'.format(list(ru_pendek[0])) % (maxJarak))
    print('c. Rute alternatif adalah ', rute_tengah, 'dengan total jarak', mid, 'km')
 
if __name__ == '__main__':
    jalanJalan(matriks, 0)