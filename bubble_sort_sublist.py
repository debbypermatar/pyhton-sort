def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [[3, 5], [1, 2], [4, 6], [2, 1]]
bubble_sort(arr)
print("Hasil pengurutan:", arr)
