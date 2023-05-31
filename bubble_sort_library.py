def bubble_sort_buku(daftar_buku):
    n = len(daftar_buku)
    for i in range(n):

        swapped = False
        for j in range(0, n-i-1):
            if daftar_buku[j]["Jumlah Halaman"] > daftar_buku[j+1]["Jumlah Halaman"]:

                daftar_buku[j], daftar_buku[j +
                                            1] = daftar_buku[j+1], daftar_buku[j]
                swapped = True

        if not swapped:
            break
    return daftar_buku


daftar_buku = [
    {"No.": 1, "Judul Buku": "Harry Potter and the Sorcerer's Stone",
        "Penulis": "J.K. Rowling", "Jumlah Halaman": 320},
    {"No.": 2, "Judul Buku": "To Kill a Mockingbird",
        "Penulis": "Harper Lee", "Jumlah Halaman": 281},
    {"No.": 3, "Judul Buku": "The Great Gatsby",
        "Penulis": "F. Scott Fitzgerald", "Jumlah Halaman": 180},
    {"No.": 4, "Judul Buku": "Pride and Prejudice",
        "Penulis": "Jane Austen", "Jumlah Halaman": 432},
    {"No.": 5, "Judul Buku": "1984", "Penulis": "George Orwell", "Jumlah Halaman": 328}
]


daftar_buku_terurut = bubble_sort_buku(daftar_buku)

# hasil pengurutan
print("Hasil pengurutan daftar buku berdasarkan jumlah halaman secara ascending:")
for buku in daftar_buku_terurut:
    print("No.:", buku["No."])
    print("Judul Buku:", buku["Judul Buku"])
    print("Penulis:", buku["Penulis"])
    print("Jumlah Halaman:", buku["Jumlah Halaman"])
    print()
