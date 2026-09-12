import math
import random
import matplotlib.pyplot as plt

from src.hybrid_sort import hybrid_sort
from src.merge_sort import merge_sort


def generate_data(n, x):
    return [random.randint(1, x) for _ in range(n)]


# Part C(i): fixed S, varying input size n
x = 10_000_000
S = 15

sizes = [
    1_000,
    3_000,
    5_000,
    7_000,
    10_000,
    30_000,
    50_000,
    70_000,
    100_000,
    300_000,
    500_000,
    700_000,
    1_000_000,
    3_000_000,
    5_000_000,
    7_000_000,
    10_000_000,
]

results_ci = []

for n in sizes:
    data = generate_data(n, x)

    sorted_data, comparisons = hybrid_sort(data, S)

    results_ci.append((n, comparisons))

    print(f"n = {n:,}, key comparisons = {comparisons:,}")

input_sizes = [result[0] for result in results_ci]
comparison_counts = [result[1] for result in results_ci]

plt.figure(figsize=(10, 6))
plt.plot(input_sizes, comparison_counts, marker="o")
plt.xlabel("Input size, n")
plt.ylabel("Number of key comparisons")
plt.title("Number of Key Comparisons vs Input Size")
plt.grid(True)
plt.tight_layout()
plt.show()


theoretical_values = [
    n * math.log2(n)
    for n in input_sizes
]

# Scale the theoretical curve so that its growth can be compared visually
# with the empirical number of key comparisons.
scale = comparison_counts[0] / theoretical_values[0]

scaled_theoretical = [
    value * scale
    for value in theoretical_values
]

plt.figure(figsize=(10, 6))
plt.plot(
    input_sizes,
    comparison_counts,
    marker="o",
    label="Empirical key comparisons",
)
plt.plot(
    input_sizes,
    scaled_theoretical,
    marker="x",
    label="Theoretical O(n log n)",
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
For a fixed threshold S, the hybrid Mergesort has a time complexity of
O(n log n). Using Insertion Sort for subarrays of size at most S does not
change the overall asymptotic complexity because S remains constant.

The empirical results should show that the number of key comparisons grows
as n increases, with an overall trend broadly consistent with O(n log n).
The exact comparison counts do not have to match n log n because Big-O
notation describes asymptotic growth rather than exact operation counts.
"""


# Part C(ii): fixed input size n, varying S
n = 100_000

S_values = [1, 2, 3, 4, 5, 10, 20, 40, 50, 100, 200, 500]

# Generate one dataset and reuse copies of it for every S value so that
# each threshold is tested on exactly the same input.
data = generate_data(n, x)

results_cii = []

for S in S_values:
    testing_data = data.copy()

    sorted_data, comparisons = hybrid_sort(testing_data, S)

    results_cii.append((S, comparisons))

    print(f"S = {S}, key comparisons = {comparisons:,}")

threshold_values = [result[0] for result in results_cii]
comparison_by_s = [result[1] for result in results_cii]

plt.figure(figsize=(10, 6))
plt.plot(threshold_values, comparison_by_s, marker="o")
plt.xlabel("S value")
plt.ylabel("Number of key comparisons")
plt.title("Number of Key Comparisons vs S Value")
plt.grid(True)
plt.tight_layout()
plt.show()


# Preliminary C(iii): best S for the single fixed dataset used in C(ii).
# The assignment still requires this to be extended across different input sizes.
best_result = min(results_cii, key=lambda result: result[1])

best_S = best_result[0]
best_comparisons = best_result[1]

print()
print(f"Best S value for n = {n:,}: {best_S}")
print(f"Lowest number of key comparisons = {best_comparisons:,}")
