def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if arr[j][0] < arr[max_index][0]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]


arr = [[3, 5], [1, 2], [4, 6], [2, 1]]
selection_sort(arr)
print("Hasil pengurutan", arr)

# melakukan
