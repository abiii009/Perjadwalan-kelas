import random

# Daftar mata kuliah
mata_kuliah = ["Algoritma", "Basis Data", "AI", "Jaringan"]

# Slot waktu yang tersedia
waktu = ["Senin 08.00", "Senin 10.00", "Selasa 08.00", "Selasa 10.00"]

# ----------------------------
# Membuat kromosom (jadwal)
# ----------------------------
def buat_kromosom():
    return [random.choice(waktu) for _ in mata_kuliah]

# ----------------------------
# Fungsi fitness
# Semakin sedikit konflik, semakin baik
# ----------------------------
def fitness(kromosom):
    konflik = len(kromosom) - len(set(kromosom))
    return 1 / (1 + konflik)

# ----------------------------
# Seleksi (Tournament Selection)
# ----------------------------
def seleksi(populasi):
    kandidat = random.sample(populasi, 3)
    kandidat.sort(key=lambda x: fitness(x), reverse=True)
    return kandidat[0]

# ----------------------------
# Crossover
# ----------------------------
def crossover(parent1, parent2):
    titik = random.randint(1, len(parent1)-1)
    child = parent1[:titik] + parent2[titik:]
    return child

# ----------------------------
# Mutasi
# ----------------------------
def mutasi(kromosom, rate=0.1):
    for i in range(len(kromosom)):
        if random.random() < rate:
            kromosom[i] = random.choice(waktu)
    return kromosom

# ----------------------------
# Inisialisasi populasi
# ----------------------------
ukuran_populasi = 10
populasi = [buat_kromosom() for _ in range(ukuran_populasi)]

# ----------------------------
# Proses Evolusi
# ----------------------------
generasi = 50

for g in range(generasi):
    populasi.sort(key=lambda x: fitness(x), reverse=True)

    if fitness(populasi[0]) == 1.0:
        break

    populasi_baru = []

    for _ in range(ukuran_populasi):
        p1 = seleksi(populasi)
        p2 = seleksi(populasi)

        anak = crossover(p1, p2)
        anak = mutasi(anak)

        populasi_baru.append(anak)

    populasi = populasi_baru

# ----------------------------
# Hasil terbaik
# ----------------------------
terbaik = max(populasi, key=fitness)

print("Jadwal Terbaik:")
for mk, slot in zip(mata_kuliah, terbaik):
    print(f"{mk:12} -> {slot}")

print("\nFitness:", fitness(terbaik))