a = 5

#Piramid Ke atas dari kanan
def pir_keatas_kanan():
    for i in range(a):
        for n in range(i + 1):
            print("*", end = " ")
        print("")

#Piramid ke bawah dari kanan
def pir_kebawah_kanan():
    for i in range(a, 0, -1):
        for n in range(i, 0, -1):
            print("*", end = " ")
        print("")

#Piramid ke atas dari kiri
def pir_keatas_kiri():
    for i in range(a, 0, -1):
        for n in range(1, a + 1):
            if n >= i:
                print("*", end = " ")
            else:
                print(" ", end = " ")
        print("")

#Piramid Penuh ke atas
def pir_keatas_penuh():
    for i in range(a, 0, -1):
        for n in range(1, a + 1):
            if n >= i:
                print("*", end = " ")
            else:
                print(" ", end = "")
        print("")

#Piramid Penuh ke bawah
def pir_kebawah_penuh():
    for i in range(a):
        for n in range(a):
            if n >= i:
                print("*", end = " ")
            else:
                print(" ", end = "")
        print("")

#Tinggal memanggil function dari atas
pir_keatas_kanan()