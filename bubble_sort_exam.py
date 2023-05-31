def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Lakukan iterasi untuk membandingkan elemen ke-i dengan elemen berikutnya
        for j in range(0, n-i-1):
            # Jika elemen saat ini lebih besar dari elemen berikutnya, tukar posisinya
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


# Daftar nilai awal
nilai = [78, 65, 90, 82, 70]

# Panggil fungsi bubble_sort untuk mengurutkan daftar nilai
nilai_terurut = bubble_sort(nilai)

# Tampilkan daftar nilai terurut
print("Daftar nilai terurut:", nilai_terurut)
