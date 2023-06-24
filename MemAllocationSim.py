import random

# Array untuk menyimpan status alokasi blok memory
memory = [
    {"index": 0, "size": 0},
    {"index": 1, "size": 0},
    {"index": 2, "size": 0},
    {"index": 3, "size": 0},
    {"index": 4, "size": 0}
]

# Update tampilan blok memory dengan angka random
def update_memory_blocks():
    for i in range(len(memory)):
        print(f"Block{i}: {memory[i]['index']}, Number{i}: {memory[i]['size']}")

# Algoritma alokasi memori berdasarkan metode yang dipilih
def allocate_memory():
    # Mendapatkan input proses dan besaran proses
    process1 = int(input("Proses 1: "))
    process2 = int(input("Proses 2: "))
    process3 = int(input("Proses 3: "))
    process4 = int(input("Proses 4: "))

    # Mendapatkan metode alokasi memori yang dipilih
    method = input("FirstFit[1]  BestFit[2]  PostFit[3]\nMetode: ")

    # Array untuk menyimpan data proses dan lokasi blok memory
    processes = [process1, process2, process3, process4]
    allocations = []

    # Mengosongkan lokasi blok memory sebelum alokasi
    for i in range(len(memory)):
        memory[i]["size"] = 0

    # Mendapatkan blok memory yang sesuai dengan metode alokasi memori
    for i in range(len(processes)):
        best_block = -1

        if method == "1":
            best_block = first_fit(processes[i])
        elif method == "2":
            best_block = best_fit(processes[i])
        elif method == "3":
            best_block = worst_fit(processes[i])

        if best_block != -1:
            memory[best_block]["size"] = processes[i]

        allocations.append(best_block)

    # Menampilkan output alokasi memori
    print("Output:")
    print("Proses\tBesaran Proses\tLokasi Blok Memory")
    for i in range(len(processes)):
        print(f"{i + 1}\t{processes[i]}\t\t{allocations[i] if allocations[i] != -1 else 'Tidak Dapat Dialokasikan'}")

    # Update tampilan blok memory
    update_memory_blocks()

def first_fit(process):
    for i in range(len(memory)):
        if memory[i]["size"] == 0 or process <= memory[i]["size"]:
            return i
    return -1

def best_fit(process):
    best_block = -1
    min_diff = float('inf')
    for i in range(len(memory)):
        if memory[i]["size"] == 0 or process <= memory[i]["size"]:
            diff = memory[i]["size"] - process
            if diff < min_diff:
                best_block = i
                min_diff = diff
    return best_block

def worst_fit(process):
    best_block = -1
    max_diff = -1
    for i in range(len(memory)):
        if memory[i]["size"] == 0 or process <= memory[i]["size"]:
            diff = memory[i]["size"] - process
            if diff > max_diff:
                best_block = i
                max_diff = diff
    return best_block

# Menginisialisasi tampilan blok memory dengan angka random
def initialize_memory_blocks():
    for i in range(len(memory)):
        memory[i]["size"] = random.randint(1, 233)
    update_memory_blocks()

# Memanggil fungsi awal untuk mengisi angka random pada blok memory
initialize_memory_blocks()

# Menjalankan simulasi alokasi memori
allocate_memory()
