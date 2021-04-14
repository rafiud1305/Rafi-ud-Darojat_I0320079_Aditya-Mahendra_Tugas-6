print('=================================')
print('Tugas 6 Soal 3')
print('=================================')

Maksimal = 24
Minimal = 10
print("Bilangan prima antara",Minimal,"dan",Maksimal)
for Nilai in range(Minimal,Maksimal + 1):
    if Nilai > 1:
        for i in range(2,Nilai):
            if (Nilai % i) == 0:
                print(Nilai,'ini bukan prima')
                break
        else:
            print(Nilai,'ini prima')