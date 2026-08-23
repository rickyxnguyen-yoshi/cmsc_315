# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Running the Program

From this directory, run:

```bash
python3 unit2_discussion.py
```

The program printed a stack demo, a queue demo, empty and single-item edge cases, and a real-world scenario (text-editor undo and a printer job line).

---

## Implementation Documentation

This section documents the completed implementation in `unit2_discussion.py`. A **stack** used a Python list with the end of the list as the top. A **queue** used `collections.deque` so enqueue and dequeue stayed efficient.

### Design Summary

| Component | Name | Purpose |
|-----------|------|---------|
| Stack | `Stack` | LIFO container: `push`, `pop`, `peek`, `is_empty` |
| Queue | `Queue` | FIFO container: `enqueue`, `dequeue`, `front`, `is_empty` |
| Stack demo | `main()` | Pushed 4 values, popped in reverse order, tested empty and single-item cases |
| Queue demo | `main()` | Enqueued 4 values, dequeued in arrival order, tested empty and single-item cases |
| Real-world scenario | `demonstrate_real_world()` | Undo history (stack) and printer jobs (queue) |

### Stack operations

Internal storage was a list named `items`. The last index was the top of the stack.

**Methods**
- `__init__(self)` — created an empty list
- `push(self, value)` — appended to the end. That supported LIFO because the last value added was the first one removed.
- `pop(self)` — removed and returned the top value. If the stack was empty, printed a message and returned `None` instead of raising an error.
- `peek(self)` — returned the top value without removing it. Empty stacks printed a message and returned `None`.
- `is_empty(self)` — returned `True` when there were no values

**LIFO behavior**

Pushing A, B, C, then D and then popping yielded D, C, B, A.

**Edge cases**
- `pop()` and `peek()` on an empty stack returned `None`
- A stack with one item was empty after that item was popped

### Queue operations

Internal storage was a `deque` named `items`. Values entered at the back and left from the front.

**Methods**
- `__init__(self)` — created an empty deque
- `enqueue(self, value)` — appended to the back. That supported FIFO because new arrivals waited behind existing items.
- `dequeue(self)` — removed and returned the front value. If the queue was empty, printed a message and returned `None`.
- `front(self)` — returned the next value that would be dequeued, without removing it. Empty queues printed a message and returned `None`.
- `is_empty(self)` — returned `True` when there were no values

**FIFO behavior**

Enqueueing first, second, third, then fourth and then dequeuing yielded first, second, third, fourth.

**Edge cases**
- `dequeue()` and `front()` on an empty queue returned `None`
- A queue with one item was empty after that item was dequeued

### Real-world scenario: `demonstrate_real_world()`

Two everyday uses of the same operations were added:

1. **Text editor undo (stack)** — each edit was pushed. Undo popped the most recent edit first, so the last change was reversed before earlier ones.
2. **Printer job line (queue)** — jobs were enqueued as they were submitted and printed in arrival order.

**Key takeaway:** Order of removal was the difference. A stack reversed arrival order; a queue preserved it.

---

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.
