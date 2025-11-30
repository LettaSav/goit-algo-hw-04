Sorting Algorithms Comparison: Timsort vs Merge Sort vs Insertion Sort
Methodology:
Input Sizes: n = 3,000 elements
Input Patterns:
- Sorted: Already in ascending order
- Random: Uniformly shuffled permutation of 0…n-1
- Reverse: Sorted in descending order
Timing: Measured using Python’s timeit module (5 runs per test)
Visualization: Results plotted with matplotlib

Key observation:
Shown in the code in the bar chart.
for the n = 3000 with 5 runs per test:
               |         Sorted           |  Random     |   Reverse   |
TimSort        |  ~0.00003 s (O(n))       | ~0.00048 s  | ~0.00004 s  | 
Merge Sort     |  ~0.00708 s (O(n log n)) | ~ 0.00858 s | ~0.00901 s  |
Insertion Sort |  ~0.00043 s (O(n))       | ~ 0.28494 s | ~0.54225 s  |

Highlights:
 - Timsort is consistently the fastest, especially on realistic data (sorted or partially ordered).
 - Insertion Sort performs well only on nearly sorted data — but degrades severely on random/reverse inputs.
 - Merge Sort is stable and predictable (O(n log n)) but not adaptive — it doesn’t exploit existing order.

In result of  the empirical evidence we have confirm next info:
 - Insertion Sort: Fast only on small or nearly sorted data (O(n²) worst case)
 - Merge Sort: Reliable but inflexible (O(n log n) always)
 - Timsort: Adaptive, efficient, and production-ready