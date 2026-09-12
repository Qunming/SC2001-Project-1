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



#This is part Ci where we run the hybrid sort with a fixed S value of 15 and varying input sizes. We will record the number of key comparisons for each input size and plot the results.
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


#This is part Cii where we run the hybrid sort with input size n fixed at 10,000,000 and varying S values. We will record the number of key comparisons for each S value and plot the results.
#Fixed input size n = 100,000   
n = 100000

#Generate a list of values for S to be tested
S_values = [1, 2, 3, 4, 5, 10, 20, 40, 50, 100, 200, 500]

#We will generate the fixed dataset to be experimented on. This ensures that the same dataset is used for each S value, allowing for a fair comparison of the number of key comparisons.
data = generate_data(n, x)

results_cii = []
for S in S_values:

    # Create a copy of the original data for each S value
    testing_data = data.copy()  
    
    sorted_data, comparisons = hybrid_sort(testing_data, S)

    results_cii.append((S, comparisons))

    print(f"S = {S}, key comparisons = {comparisons:,}")

S_values_array = [result[0] for result in results_cii]
comparison_s_array = [result[1] for result in results_cii]


#plot graph of number of key comparisons vs S value
plt.figure(figsize=(10, 6))

plt.plot(
    S_values_array,
    comparison_s_array,
    marker='o'
)

plt.xlabel("S value")
plt.ylabel("Number of key comparisons")
plt.title("Number of Key Comparisons vs S Value")

plt.grid(True)
plt.tight_layout()

plt.show()



#Ciii Look for the S value that results in the lowest number of key comparisons

"""
best_result = min(results_cii, key=lambda result: result[1])

best_S = best_result[0]
best_comparisons = best_result[1]

print()
print(f"Best S value = {best_S}")
print(f"Lowest number of key comparisons = {best_comparisons:,}")
"""


# =========================================================
# Part C(iii)
# Test different input sizes to study the optimal S value
# =========================================================

n_values_ciii = [
    10000,
    100000,
    1000000
]

S_values_ciii = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    12, 15, 20, 25, 30
]

results_ciii = []

for n_test in n_values_ciii:

    print()
    print(f"Testing n = {n_test:,}")

    data = generate_data(n_test, x)

    for S_test in S_values_ciii:

        testing_data = data.copy()

        sorted_data, comparisons = hybrid_sort(
            testing_data,
            S_test
        )

        results_ciii.append(
            (
                n_test,
                S_test,
                comparisons
            )
        )

        print(
            f"n = {n_test:,}, "
            f"S = {S_test}, "
            f"comparisons = {comparisons:,}"
        )


print()
print("Best S value for each input size")

best_S_results = []

for n_test in n_values_ciii:

    results_for_n = [
        result
        for result in results_ciii
        if result[0] == n_test
    ]

    best_result = min(
        results_for_n,
        key=lambda result: result[2]
    )

    best_n = best_result[0]
    best_S = best_result[1]
    best_comparisons = best_result[2]

    best_S_results.append(
        (
            best_n,
            best_S,
            best_comparisons
        )
    )

    print(
        f"n = {best_n:,}, "
        f"best S = {best_S}, "
        f"comparisons = {best_comparisons:,}"
    )


plt.figure(figsize=(10, 6))

for n_test in n_values_ciii:

    S_for_n = []
    comparisons_for_n = []

    for result in results_ciii:

        if result[0] == n_test:

            S_for_n.append(result[1])
            comparisons_for_n.append(result[2])

    plt.plot(
        S_for_n,
        comparisons_for_n,
        marker='o',
        label=f"n = {n_test:,}"
    )

plt.xlabel("S value")
plt.ylabel("Number of key comparisons")
plt.title(
    "Number of Key Comparisons vs S "
    "for Different Input Sizes"
)

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()