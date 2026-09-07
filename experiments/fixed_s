import random
import matplotlib.pyplot as plt
import math

def generate_data(n, x):
    return [random.randint(1, x) for _ in range(n)]

def insertion_sort(A):

    n = len(A)
    comparisons = 0

    for i in range(1, n):

        j = i - 1

        while j >= 0:

            comparisons += 1

            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                j -= 1
            else:
                break

    return A, comparisons


def hybrid_sort(A, S):

    if len(A) <= S:
        return insertion_sort(A)

    middle = len(A) // 2

    left = A[:middle]
    right = A[middle:]

    left, left_comparisons = hybrid_sort(left, S)
    right, right_comparisons = hybrid_sort(right, S)

    result, merge_comparisons = merge(left, right)

    total_comparisons = (
        left_comparisons
        + right_comparisons
        + merge_comparisons
    )

    return result, total_comparisons


def merge(left, right):

    result = []
    i = 0
    j = 0

    comparisons = 0

    while i < len(left) and j < len(right):

        comparisons += 1

        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result, comparisons




x = 10000000
S = 15

size = [
    1000,
    3000,
    5000,
    7000,
    10000,
    30000,
    50000,
    70000,
    100000,
    300000,
    500000,
    700000,
    1000000,
    3000000,
    5000000,
    7000000,
    10000000
]

results = []

for n in size:
    data = generate_data(n, x)

    sorted_data, comparisons = hybrid_sort(data, S)

    results.append((n, comparisons))

    print(f"n = {n:,}, key comparisons = {comparisons:,}")

array = [result[0] for result in results]
comparison = [result[1] for result in results]

plt.figure(figsize=(10, 6))

plt.plot(
    array,
    comparison,
    marker='o'
)

plt.xlabel("Input size, n")
plt.ylabel("Number of key comparisons")
plt.title("Number of Key Comparisons vs Input Size")

plt.grid(True)
plt.tight_layout()

plt.show()

theoretical_values = [
    n * math.log2(n)
    for n in array
]

# Scale theoretical curve to make it comparable
scale = comparison[0] / theoretical_values[0]

scaled_theoretical = [
    value * scale
    for value in theoretical_values
]

plt.figure(figsize=(10, 6))

plt.plot(
    array,
    comparison,
    marker='o',
    label="Empirical key comparisons"
)

plt.plot(
    array,
    scaled_theoretical,
    marker='x',
    label="Theoretical O(n log n)"
)

plt.xscale("log")

plt.xlabel("Input size, n")
plt.ylabel("Number of key comparisons")
plt.title("Empirical Results vs Theoretical O(n log n)")

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
""" 
The theoretical results shows that hybrid merge sort has a time complexity of O(nlogn). The use of insertion sort for subarrays of size at most S does not change the overall complexity because S is fixed.
The empirical results shows that the number of key comparison increases when the input increases. Overall, the growth of the empirical results is broadly consistent with the theoretical analysis of the hybrid sort. The actual number of comparisons does not exactly match O(nlogn) is expected as Big-O notation describes the asymptotic growth rate rather than the exact numbers of comparison.
Therefore, the experimental results provide evidence supporting the theoretical conclusion that the hybrid merge sort has a time complexity of O(nlogn)
"""
