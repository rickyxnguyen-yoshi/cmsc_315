"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # The end of the list is the top of the stack.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Append adds to the end (the top). The last item pushed is the first
        # one popped, which is LIFO (Last In, First Out).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # If the stack is empty, return None instead of raising an error so
        # callers can handle the empty case without crashing.
        if self.is_empty():
            print("  (pop on empty stack: nothing to remove)")
            return None
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Peek returns the top value without removing it, so you can inspect
        # the next item that would be popped without changing the stack.
        if self.is_empty():
            print("  (peek on empty stack: no top value)")
            return None
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # deque supports O(1) add/remove at both ends, which is a good fit
        # for a queue (enqueue at the back, dequeue from the front).
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Add to the back. New arrivals wait behind existing items, so the
        # first item enqueued is the first one dequeued (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # If the queue is empty, return None instead of raising an error.
        if self.is_empty():
            print("  (dequeue on empty queue: nothing to remove)")
            return None
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Front returns the next value that would be dequeued, without
        # removing it from the queue.
        if self.is_empty():
            print("  (front on empty queue: no front value)")
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def demonstrate_real_world():
    """
    Real-world scenario: undo in a text editor (stack) and a print job
    line (queue).
    """
    print("\n=== REAL-WORLD SCENARIO ===")

    print("\nText editor undo (stack / LIFO):")
    print("Each edit is pushed. Undo pops the most recent edit first.")
    undo_stack = Stack()
    edits = ["typed 'Hello'", "typed ' world'", "bold last word", "added '!'"]
    for edit in edits:
        undo_stack.push(edit)
        print(f"  Edit: {edit}")
    print(f"  Latest edit (peek): {undo_stack.peek()}")
    while not undo_stack.is_empty():
        print(f"  Undo: {undo_stack.pop()}")
    print(f"  All edits undone. Stack empty? {undo_stack.is_empty()}")

    print("\nPrinter job line (queue / FIFO):")
    print("Jobs are served in the order they arrived.")
    printer = Queue()
    jobs = ["Syllabus.pdf", "Lab2.py", "Resume.docx", "Notes.md"]
    for job in jobs:
        printer.enqueue(job)
        print(f"  Submitted: {job}")
    print(f"  Next to print (front): {printer.front()}")
    while not printer.is_empty():
        print(f"  Printing: {printer.dequeue()}")
    print(f"  All jobs printed. Queue empty? {printer.is_empty()}")


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("\n=== STACK DEMO ===")
    stack = Stack()
    print("Created an empty stack.")

    values = ["A", "B", "C", "D"]
    for value in values:
        stack.push(value)
        print(f"  Pushed '{value}'. Top is now '{stack.peek()}'.")

    print("\nPopping values (LIFO: D comes out before A):")
    while not stack.is_empty():
        print(f"  Popped '{stack.pop()}'.")

    print("\nEmpty-stack edge cases:")
    print(f"  pop() returned: {stack.pop()}")
    print(f"  peek() returned: {stack.peek()}")

    print("\nSingle-item stack:")
    one_item = Stack()
    one_item.push("only")
    print(f"  Pushed 'only'. Empty? {one_item.is_empty()}")
    print(f"  Popped '{one_item.pop()}'. Empty afterward? {one_item.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    queue = Queue()
    print("Created an empty queue.")

    values = ["first", "second", "third", "fourth"]
    for value in values:
        queue.enqueue(value)
        print(f"  Enqueued '{value}'. Front is still '{queue.front()}'.")

    print("\nDequeuing values (FIFO: 'first' comes out before 'fourth'):")
    while not queue.is_empty():
        print(f"  Dequeued '{queue.dequeue()}'.")

    print("\nEmpty-queue edge cases:")
    print(f"  dequeue() returned: {queue.dequeue()}")
    print(f"  front() returned: {queue.front()}")

    print("\nSingle-item queue:")
    one_item = Queue()
    one_item.enqueue("only")
    print(f"  Enqueued 'only'. Empty? {one_item.is_empty()}")
    print(f"  Dequeued '{one_item.dequeue()}'. Empty afterward? {one_item.is_empty()}")

    demonstrate_real_world()


if __name__ == "__main__":
    main()
