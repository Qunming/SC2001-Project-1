## Expected End Product

The completed project should contain a working implementation and experimental analysis of:

1. Standard Merge Sort
2. Insertion Sort
3. Hybrid Merge Sort + Insertion Sort

The hybrid algorithm should use a threshold value `S`:

- If the current subarray size is greater than `S`, continue using Merge Sort.
- If the current subarray size is less than or equal to `S`, switch to Insertion Sort.

### Final Project Structure

```text
SC2001-Project-1/
├── src/
│   ├── merge_sort.py
│   ├── insertion_sort.py
│   └── hybrid_sort.py
│
├── experiments/
│   ├── vary_n.py
│   ├── vary_s.py
│   └── final_comparison.py
│
├── results/
│   ├── data/
│   └── graphs/
│
├── README.md
└── .gitignore
```

### Program Requirements

The final implementation should be able to:

- Sort an array correctly using standard Merge Sort.
- Sort an array correctly using Insertion Sort.
- Sort an array using the hybrid Merge Sort + Insertion Sort algorithm.
- Allow the threshold value `S` to be changed.
- Count the number of key comparisons performed.
- Measure CPU execution time where required.

### Experiments

The final project should include the following experiments.

#### 1. Fixed `S`, Different Input Sizes `n`

Keep `S` constant while increasing the size of the input array.

Record:

- Input size `n`
- Threshold `S`
- Number of key comparisons

Plot:

```text
x-axis: Input size n
y-axis: Number of key comparisons
```

Compare the experimental results with the theoretical time complexity.

#### 2. Fixed `n`, Different Values of `S`

Keep the input size `n` constant while changing `S`.

Record:

- Input size `n`
- Threshold `S`
- Number of key comparisons

Plot:

```text
x-axis: Threshold S
y-axis: Number of key comparisons
```

Compare the experimental results with the theoretical analysis.

#### 3. Determine an Optimal `S`

Test different values of `S` using different input sizes.

Use the experimental results to investigate which value or range of values of `S` gives the best performance.

#### 4. Hybrid Sort vs Standard Merge Sort

Using a dataset containing 10 million integers, compare:

```text
Standard Merge Sort
vs
Hybrid Merge Sort + Insertion Sort
```

Compare both algorithms using:

- Number of key comparisons
- CPU execution time

The hybrid algorithm should use the selected optimal value of `S`.

### Final Results

The completed project should therefore produce:

- Correctly sorted datasets
- Key-comparison counts
- CPU-time measurements
- Graph of key comparisons against input size `n`
- Graph of key comparisons against threshold `S`
- Analysis of an optimal `S`
- Final comparison between standard Merge Sort and the hybrid algorithm