# SC2001 Project 1 — Integration of Mergesort & Insertion Sort

This project implements and analyses a hybrid sorting algorithm that combines Mergesort with Insertion Sort.

For small subarrays, the overhead of repeated recursive Mergesort calls can reduce efficiency. The hybrid algorithm therefore uses a threshold value `S`:

- If the current subarray size is greater than `S`, continue using Mergesort.
- If the current subarray size is less than or equal to `S`, switch to Insertion Sort.

The project studies how input size `n` and threshold `S` affect the number of key comparisons and overall performance.

## Assignment Requirements

### (a) Hybrid Algorithm

Implement the hybrid Mergesort–Insertion Sort algorithm using a threshold `S`.

### (b) Input Data Generation

Generate random integer arrays with input sizes ranging from 1,000 to 10,000,000.

Each integer is generated in the range `[1, x]`, where `x` is the maximum allowed integer value.

### (c) Time Complexity Analysis

#### (i) Fixed `S`, varying `n`

Run the hybrid algorithm with a fixed threshold while increasing input size `n`.

Record and plot the number of key comparisons against `n`, then compare the empirical results with the theoretical time complexity.

Current implementation uses:

```text
S = 15
n = 1,000 ... 10,000,000
```

The empirical results are compared against the expected `O(n log n)` growth.

#### (ii) Fixed `n`, varying `S`

Keep `n` fixed while testing different threshold values:

```text
S = 1, 2, 3, 4, 5, 10, 20, 40, 50, 100, 200, 500
```

The same generated dataset is copied for every value of `S` so that the comparison is fair.

The number of key comparisons is plotted against `S`.

#### (iii) Determine an optimal `S`

Use different input dataset sizes to study which value or range of values of `S` gives the best performance.

**Status: In progress.**

The current code can identify the value of `S` with the lowest number of key comparisons for one fixed input size. The next step is to repeat this experiment across multiple input sizes before selecting an overall optimal threshold.

### (d) Hybrid Sort vs Original Mergesort

Using a dataset containing 10,000,000 integers, compare:

```text
Original Mergesort
vs
Hybrid Mergesort + Insertion Sort
```

The comparison must include:

- Number of key comparisons
- CPU execution time

The hybrid algorithm should use the optimal value of `S` obtained from Part (c).

**Status: To be implemented.**

## Current Experiment

The main experiment file is:

```text
experiments/
└── fixed_s.py
```

`fixed_s.py` currently contains:

- Random dataset generation
- Insertion Sort
- Hybrid Mergesort
- Merge operation
- Key-comparison counting
- Part C(i): fixed `S`, varying `n`
- Empirical vs theoretical `O(n log n)` comparison
- Part C(ii): fixed `n`, varying `S`
- Preliminary search for the best `S`

## Key Comparisons

A key comparison is a comparison between values from the input array.

For example, Insertion Sort counts:

```python
A[j] > A[j + 1]
```

and the merge operation counts:

```python
left[i] <= right[j]
```

Loop-control and index checks are not counted as key comparisons.

## Running the Experiment

From the project root directory:

```bash
python experiments/fixed_s.py
```

Install Matplotlib if required:

```bash
pip install matplotlib
```

## Current Progress

| Task | Status |
|---|---|
| Hybrid algorithm implementation | Completed |
| Random input generation | Completed |
| Key-comparison counting | Completed |
| C(i): Fixed `S`, varying `n` | Completed |
| C(i): Empirical vs theoretical analysis | Completed |
| C(ii): Fixed `n`, varying `S` | Implemented |
| C(ii): Theoretical analysis | In progress |
| C(iii): Optimal `S` using different `n` | In progress |
| Part (d): Hybrid vs original Mergesort | To do |
| Part (d): CPU-time comparison | To do |
