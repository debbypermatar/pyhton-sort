def selection_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return count


arr = [64, 34, 25, 12, 22, 11, 90]
iterations = selection_sort(arr)
print("Hasil pengurutan", arr)
print("Jumlah iterasi", iterations)
