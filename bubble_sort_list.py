def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Daftar angka yang dimiliki oleh Andi
angka_andi = [9, 5, 3, 8, 2]

# Menggunakan Selection Sort untuk mengurutkan daftar angka
selection_sort(angka_andi)

# Menampilkan hasil pengurutan
print("Hasil pengurutan angka Andi:", angka_andi)
