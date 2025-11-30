import timeit
import random
import matplotlib.pyplot as plt
import numpy as np

# Insertion Sort Implementation
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    # Find the midpoint
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

# Merge helper function
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    # Merge the two halves
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Append any remaining elements
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    # Append any remaining elements
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


#Generate 3 datasets
number_of_runs = 5
base = list(range(3000))
datasets = {
    "Sorted": base[:],
    "Random":  [random.randint(1, 3000) for _ in range(3000)],
    "Reverse": base[::-1]
}

algorithms = ["Timsort", "MergeSort", "Insertion"]
results = {pattern: [] for pattern in datasets}

# Benchmark All Combinations 
for pattern_name, data in datasets.items():
    print(f"Benchmarking on {pattern_name} data...")
    
  # Timsort
    t1 = timeit.timeit(
        lambda: sorted(data.copy()),
        number=number_of_runs
    ) / number_of_runs
    results[pattern_name].append(t1)
    
    # Merge Sort
    t2 = timeit.timeit(
        lambda: merge_sort(data.copy()),
        number=number_of_runs
    ) / number_of_runs
    results[pattern_name].append(t2)
    
    # Insertion Sort
    t3 = timeit.timeit(
        lambda: insertion_sort(data.copy()),
        number=number_of_runs
    ) / number_of_runs
    results[pattern_name].append(t3)

patterns = list(datasets.keys())
x = np.arange(len(patterns))  # label locations
width = 0.25  # bar width

fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars for each algorithm
bars1 = ax.bar(x - width, [results[p][0] for p in patterns], width, label='Timsort', color = '#4CAF50')
bars2 = ax.bar(x,        [results[p][1] for p in patterns], width, label='MergeSort', color='#2196F3')
bars3 = ax.bar(x + width, [results[p][2] for p in patterns], width, label='Insertion', color="#F4B136")

# Labels and title
ax.set_xlabel('Input Pattern')
ax.set_ylabel('Average Time (seconds)')
ax.set_title(f'Sorting Algorithm Comparison (n = {3000:,}). Number of runs = {number_of_runs}')
ax.set_xticks(x)
ax.set_xticklabels(patterns)
ax.legend()

# Add value labels on bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.5f}s',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

fig.tight_layout()
plt.show()