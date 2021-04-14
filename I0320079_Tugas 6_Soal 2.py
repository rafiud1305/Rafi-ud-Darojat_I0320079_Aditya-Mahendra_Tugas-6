print('=================================')
print('Tugas 6 Soal 2')
print('=================================')

#rumus1
Nilai = input('Masukan semua nilai (gunakan koma untuk pemisah):')
Daftar_Nilai = Nilai.split(',')
Nilai_Akhir = [int(x) for x in Daftar_Nilai]
total = 0

#rumus2
for nilai in Nilai_Akhir :
    total = total + nilai
Rata_Rata = total / len(Nilai_Akhir)

#tampilan
print('Jumlah nilai anda', total)
print('Rata-rata nilai keseluruhan:', Rata_Rata)