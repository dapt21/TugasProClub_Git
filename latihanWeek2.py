"""
Untuk menjalankan program, hapus lah command komentar program yang menggunakan "
dan setelah di hapus, program sebelumnya gunakan lagi command komentar "
"""

#Mencari angka kemunculan (soal 1)
"""
def angka_muncul_sekali(b):
    c = []
    cek = False
    for i in range(len(b)):
        for n in range(len(b)):
            if i != n and b[i] == b[n]:
                cek = False
                break
            else:
                cek = True

        c.append(b[i]) if cek else ""
        
    return list(map(int, c))

a = list(input())
print(angka_muncul_sekali(a))
"""

#Menjumlahkan angka (soal 2)
#penginputan data menggunakan spasi (contoh: 1 2 3 4 11 20 30)
"""
def jumlah_angka(c, d):
    c = list(map(int, c))
    e = []
    for i in range(len(c)):
        for n in range(len(c)):
            if i != n and (c[i] + c[n]) == d:
                e.append(i)
    return e

a = input().split()
b = int(input("Target : "))
print(jumlah_angka(a, b))
"""

#Total kemunculan (soal 3)
"""
def muncul(b):
    c = dict()

    for i in b:
        c[i] = c.get(i, 0) + 1
        
    return c

a = input().split()

for i, n in muncul(a).items():
    print(f"{i}: {n}")
"""