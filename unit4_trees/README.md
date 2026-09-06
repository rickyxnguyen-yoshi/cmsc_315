# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Running the Program

From this directory, run:

```bash
python3 unit4_discussion.py
```

The program prints tree construction, in-order traversal, search tests, edge cases, and a real-world campus ID lookup.

---

## Implementation Documentation

This section documents the completed implementation in `unit4_discussion.py`. A **binary search tree** stores each value in a node with at most two children. Every value in a node's left subtree is smaller than the node; every value in the right subtree is larger. That ordering is what makes insert, search, and in-order traversal work.

### Design Summary

| Component | Name | Purpose |
|-----------|------|---------|
| Node | `Node` | Holds `value`, `left`, and `right` |
| Tree | `BST` | Empty tree with `root`; insert, search, in-order |
| Insert | `insert` / `_insert_recursive` | Walk left or right, then attach a new node |
| Search | `search` / `_search_recursive` | Walk left or right until found or `None` |
| Traversal | `inorder` / `_inorder_recursive` | Left, node, right (sorted keys) |
| Demos | `main()` | Build, traverse, search, edge cases |
| Real-world scenario | `demonstrate_real_world()` | Campus ID lookup |

### Node and empty tree

`Node` stores a value and starts with `left` and `right` as `None`. `BST.__init__` sets `root` to `None`. The first `insert` creates the root; later inserts attach new nodes as children.

### Insertion: `insert(value)`

`insert` calls `_insert_recursive` starting at the root.

- If the current node is `None`, a new `Node` is created at that slot.
- If the value is smaller than the current node, recursion continues on the **left**.
- If the value is larger or equal, recursion continues on the **right**.

Each comparison picks one child, so the other subtree is never visited. Duplicates are sent right so every insert still produces a valid tree.

**Tests in `main()`**

Values inserted: `50, 30, 70, 20, 40, 60, 80, 25`

- `50` is the root
- `30`, `20`, `40`, and `25` go into the left subtree
- `70`, `60`, and `80` go into the right subtree

### Search: `search(value)`

Recursive search compares the target to the current node:

- Equal: return `True`
- Smaller: only the left subtree can contain it
- Larger: only the right subtree can contain it
- `None`: the value is not in the tree, return `False`

That is why BST search is often faster than linear search. Linear search checks every element. A reasonably balanced BST discards about half of the remaining nodes at each step, which is **O(log n)** instead of **O(n)**. A completely skewed tree (already sorted inserts) can still degrade to O(n).

**Tests in `main()`**
- Present: `40`, `80` → `True`
- Absent: `15`, `99` → `False`

### In-order traversal: `inorder()`

Visit the left subtree, then the current node, then the right subtree. Because left keys are smaller and right keys are larger, the visit order is sorted from smallest to largest without a separate sort.

**Test in `main()`**

In-order of the constructed tree: `[20, 25, 30, 40, 50, 60, 70, 80]`

### Edge cases

1. **Empty tree** — in-order returns `[]`; search returns `False`
2. **One-node tree** — in-order is that single value; search finds it and rejects a missing value
3. **Duplicate insert** — a second `50` is stored on the right of the existing `50`, so in-order shows `50` twice

### Real-world scenario: `demonstrate_real_world()`

A **campus ID lookup** stores student IDs in a BST:

1. Several IDs are inserted (both smaller and larger than the first ID)
2. In-order prints enrolled IDs from low to high
3. Search confirms an enrolled ID and rejects one that is not enrolled

**Key takeaway:** Ordering is built into the tree. Each comparison throws away a whole subtree, which is how a BST reduces search space compared with scanning a list.

---

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
