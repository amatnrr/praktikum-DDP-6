# input jumlah baris
jumlah_baris = int(input("Masukkan jumlah baris: "))

# looping untuk mencetak pola
for i in range(1, jumlah_baris + 1):
    for j in range(i):
        print('28', end='')
    print()  # Pindah ke baris berikutnya
