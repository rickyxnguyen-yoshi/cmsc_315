"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time


def linear_search(lst, target):
    """
    Scan the list from left to right until the target is found.

    Time complexity is O(n) because each comparison checks only one
    element. In the worst case (missing item, or the last item) the
    loop runs n times. There is no ordering assumption, so nothing
    can be skipped.
    """
    for i in range(len(lst)):
        # One comparison per index: after k steps, n - k items remain.
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    Search a sorted list by repeatedly cutting the remaining range in half.

    Each iteration compares the target to the middle element, then
    discards either the left half or the right half. That shrinks the
    search space from n to n/2 to n/4 ... until one item (or none)
    remains, which is O(log n) comparisons.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        # Mid splits [low, high] into two halves of about equal size.
        if lst[mid] == target:
            return mid
        if lst[mid] < target:
            # Target is larger, so every index <= mid can be ignored.
            low = mid + 1
        else:
            # Target is smaller, so every index >= mid can be ignored.
            high = mid - 1

    return -1


def count_linear_steps(lst, target):
    """Same scan as linear_search, but also return how many checks ran."""
    steps = 0
    for i in range(len(lst)):
        steps += 1
        if lst[i] == target:
            return i, steps
    return -1, steps


def count_binary_steps(lst, target):
    """Same halving as binary_search, but also return how many checks ran."""
    steps = 0
    low = 0
    high = len(lst) - 1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid, steps
        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps


def demonstrate_real_world():
    """
    Real-world scenario: looking up a product SKU in a warehouse catalog.

    A clerk can walk the catalog page by page (linear search) or jump to
    the middle of a sorted SKU list (binary search). Both find the same
    item; binary search uses far fewer comparisons once the catalog is
    sorted.
    """
    print("\n=== REAL-WORLD SCENARIO: WAREHOUSE SKU LOOKUP ===")
    print("Product SKUs are stored in sorted order so a lookup can skip")
    print("whole ranges of the catalog instead of checking every item.")

    catalog = [1024, 1108, 1550, 2108, 3310, 4521, 6104, 7803, 9002]
    print(f"\nSorted SKU catalog: {catalog}")

    in_stock = 3310
    not_carried = 9999

    linear_index, linear_steps = count_linear_steps(catalog, in_stock)
    binary_index, binary_steps = count_binary_steps(catalog, in_stock)
    print(f"Lookup SKU {in_stock} (in stock):")
    print(f"  linear_search -> index {linear_index} after {linear_steps} checks")
    print(f"  binary_search -> index {binary_index} after {binary_steps} checks")

    missing_linear, missing_linear_steps = count_linear_steps(catalog, not_carried)
    missing_binary, missing_binary_steps = count_binary_steps(catalog, not_carried)
    print(f"Lookup SKU {not_carried} (not carried):")
    print(f"  linear_search -> {missing_linear} after {missing_linear_steps} checks")
    print(f"  binary_search -> {missing_binary} after {missing_binary_steps} checks")
    print("Tradeoff: linear search works on an unsorted shelf list;")
    print("binary search needs a sorted catalog but scales much better.")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    # A short sorted list makes it easy to see that both algorithms
    # return the same index when the value exists, and -1 when it does not.

    print("\n=== SMALL DATASET TEST ===")
    small = [3, 8, 12, 19, 27, 35, 42]
    print(f"Sorted dataset: {small}")

    found_target = 19
    missing_target = 20
    print(f"Search for {found_target} (exists):")
    print(f"  linear_search: {linear_search(small, found_target)}")
    print(f"  binary_search: {binary_search(small, found_target)}")
    print("Both return index 3, the position of 19.")

    print(f"Search for {missing_target} (does not exist):")
    print(f"  linear_search: {linear_search(small, missing_target)}")
    print(f"  binary_search: {binary_search(small, missing_target)}")
    print("Both return -1 because 20 is not in the list.")

    # ===============================
    # LARGE DATASET
    # ===============================
    # With one million sorted integers, linear search still walks toward
    # the target one step at a time. Binary search cuts the remaining
    # range in half each comparison, so it stays near 20 checks even
    # when n is huge.

    print("\n=== LARGE DATASET TEST ===")
    n = 1_000_000
    large = list(range(n))
    last_value = n - 1
    absent_value = n + 5
    print(f"Sorted dataset size: {n}")
    print(f"Searching for last value {last_value} and missing value {absent_value}.")

    linear_index, linear_steps = count_linear_steps(large, last_value)
    binary_index, binary_steps = count_binary_steps(large, last_value)
    print(f"Found {last_value}:")
    print(f"  linear_search index {linear_index} after {linear_steps} checks")
    print(f"  binary_search index {binary_index} after {binary_steps} checks")

    start = time.perf_counter()
    linear_search(large, last_value)
    linear_time = time.perf_counter() - start
    start = time.perf_counter()
    binary_search(large, last_value)
    binary_time = time.perf_counter() - start
    print(f"  linear_search time: {linear_time:.6f} seconds")
    print(f"  binary_search time: {binary_time:.6f} seconds")

    _, linear_miss_steps = count_linear_steps(large, absent_value)
    _, binary_miss_steps = count_binary_steps(large, absent_value)
    print(f"Missing {absent_value}:")
    print(f"  linear_search checks: {linear_miss_steps} (must scan the whole list)")
    print(f"  binary_search checks: {binary_miss_steps} (still about log2(n))")
    print("Binary search becomes more efficient as n grows because")
    print("O(log n) stays small while O(n) grows with the dataset.")

    # ===============================
    # EDGE CASES
    # ===============================
    # Empty list, one-element list, first position, and last position.

    print("\n=== EDGE CASE TESTS ===")

    empty = []
    print("Empty list:")
    print(f"  linear_search([], 5): {linear_search(empty, 5)} (expected -1)")
    print(f"  binary_search([], 5): {binary_search(empty, 5)} (expected -1)")
    print("No elements to inspect, so both searches fail immediately.")

    single = [7]
    print("Single-element list [7]:")
    print(f"  linear_search for 7: {linear_search(single, 7)}")
    print(f"  binary_search for 7: {binary_search(single, 7)}")
    print(f"  linear_search for 1: {linear_search(single, 1)}")
    print(f"  binary_search for 1: {binary_search(single, 1)}")
    print("The only comparison either matches that one value or does not.")

    print("First and last positions in the small dataset:")
    print(f"  first value 3: linear={linear_search(small, 3)}, "
          f"binary={binary_search(small, 3)}")
    print(f"  last value 42: linear={linear_search(small, 42)}, "
          f"binary={binary_search(small, 42)}")
    print("Linear search is cheapest at the front and most expensive")
    print("at the end. Binary search cost stays similar either way.")

    demonstrate_real_world()


if __name__ == "__main__":
    main()
