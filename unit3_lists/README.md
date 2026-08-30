# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

Complete all TODO sections:

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Running the Program

From this directory, run:

```bash
python3 unit3_discussion.py
```

The program prints insertion tests, deletion tests, search tests, edge cases, and a real-world class waitlist scenario.

---

## Implementation Documentation

This section documents the completed implementation in `unit3_discussion.py`. Python lists are contiguous arrays. Inserting or deleting in the middle shifts later elements; searching walks the list from the start.

### Design Summary

| Component | Name | Purpose |
|-----------|------|---------|
| Insert | `insert_at(lst, index, value)` | Inserts a value and shifts later elements right |
| Delete | `delete_at(lst, index)` | Removes a value at a valid index; returns `None` if invalid |
| Search | `search_value(lst, value)` | Linear search; returns index or `-1` |
| Demos | `main()` | Beginning / middle / end insert and delete, search, edge cases |
| Real-world scenario | `demonstrate_real_world()` | Class waitlist using the same three operations |

### Insertion: `insert_at(lst, index, value)`

Uses `list.insert`. Elements at `index` and after it move one position to the right so the new value can occupy that slot.

**Performance**
- Beginning or middle: O(n), because every later element must shift
- End: amortized O(1), because existing elements do not move

**Tests in `main()`**

Starting list: `[10, 20, 30, 40]`

1. Insert `5` at index `0` (beginning)
2. Insert `25` at the middle index
3. Insert `50` at the end

### Deletion: `delete_at(lst, index)`

Validates the index, then uses `list.pop`. If the index is negative or past the last element, the function returns `None` instead of raising `IndexError`.

Safe deletion matters because a bad index (empty list, typo, stale length) would otherwise crash the program. Returning `None` lets the caller handle the failure.

**Performance**
- Beginning or middle: O(n), remaining elements shift left to close the gap
- End: O(1), nothing after the removed item needs to move

**Tests in `main()`**

Deletes from the beginning, the middle, and the end of the list produced by the insertion tests. Each step prints the removed value and the updated list.

### Search: `search_value(lst, value)`

Linear search: start at index `0` and compare each element in order until a match is found or the list ends. Lists do not store a map from value to index, so there is no shortcut. Worst-case time is O(n).

**Return values**
- Index of the first match if the value exists
- `-1` if the value is not in the list

**Tests in `main()`**
- Search for `20` (present)
- Search for `99` (absent)

### Edge cases

1. **Invalid index** — `delete_at` with index `100` returns `None`; the list is unchanged
2. **Empty list delete** — `delete_at([], 0)` returns `None`
3. **Empty list insert** — inserting into `[]` at index `0` produces a one-element list

### Real-world scenario: `demonstrate_real_world()`

A **class waitlist** uses the same operations:

1. Priority enrollment inserts at the front (everyone else shifts right)
2. A regular add inserts at the end (no shift)
3. A mid-list insert places a student at a specific position
4. A seat opening deletes from the front
5. Search finds a student who is still waiting and reports `-1` for one who already got a seat

**Key takeaway:** Where an operation happens in the list changes both the result (who moves) and the cost (how many elements shift). Search always scans in order.

---

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?
