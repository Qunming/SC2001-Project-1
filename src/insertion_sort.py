def insertion_sort(A):
    n = len(A)

    for i in range(1, n):
        j = i - 1

        while j >= 0 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1

    return A

