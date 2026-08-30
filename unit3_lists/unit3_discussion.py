"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.

    Existing elements at and after that index shift one position to the
    right so the new value can occupy the requested slot.

    Performance depends on where the insertion occurs. Inserting at the
    front or in the middle is O(n) because every later element must move.
    Inserting at the end is amortized O(1) because nothing needs to shift.
    """
    # list.insert shifts elements at index and beyond one slot to the right.
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.

    Index validation is important because an out-of-range index would
    raise IndexError and crash the caller. Safe deletion lets the program
    handle bad input (empty list, negative index, index past the end)
    and keep running instead of failing.
    """
    # Reject invalid indexes so pop() is never called unsafely.
    if index < 0 or index >= len(lst):
        return None
    return lst.pop(index)


def search_value(lst, value):
    """
    Search for a value within the list.

    This is a linear search: it starts at index 0 and checks each
    element in order until it finds a match or reaches the end.
    Lists do not keep a lookup table of values, so there is no way
    to jump to the target. Sequential scanning is required, which
    is O(n) in the worst case.
    """
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def demonstrate_real_world():
    """
    Real-world scenario: a class waitlist.

    Students join at different positions (priority enrollment at the
    front, a typical add at the end, a waitlist insert in the middle).
    Dropping a course removes a name. Looking someone up uses search.
    """
    print("\n=== REAL-WORLD SCENARIO: CLASS WAITLIST ===")
    print("A waitlist is a list: order matters, and people move when")
    print("someone is inserted or dropped.")

    waitlist = ["Jordan", "Sam", "Riley"]
    print(f"\nStarting waitlist: {waitlist}")

    # Priority enrollment: insert at the beginning. Everyone else shifts right.
    insert_at(waitlist, 0, "Alex")
    print(f"Priority add at front (Alex): {waitlist}")

    # Regular add: insert at the end. No existing names need to shift.
    insert_at(waitlist, len(waitlist), "Taylor")
    print(f"Regular add at end (Taylor): {waitlist}")

    # A student is placed in the middle of the waitlist.
    insert_at(waitlist, 2, "Casey")
    print(f"Mid-list insert (Casey at index 2): {waitlist}")

    # First on the list gets a seat; remove from the front.
    seated = delete_at(waitlist, 0)
    print(f"Seat opened; removed '{seated}' from the front: {waitlist}")

    # Look up a student who is still waiting, then one who already left.
    found = search_value(waitlist, "Riley")
    print(f"Search for Riley (still waiting): index {found}")
    missing = search_value(waitlist, "Alex")
    print(f"Search for Alex (already seated): {missing} (not on the list)")


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    # Create a list, show it, then insert at the beginning, middle, and end.
    # Each insert shifts later elements right (except an insert at the end).

    print("\n=== INSERTION TESTS ===")
    numbers = [10, 20, 30, 40]
    print(f"Original list: {numbers}")

    # Insert at the beginning: every existing element shifts one index right.
    insert_at(numbers, 0, 5)
    print(f"After insert at beginning (index 0, value 5): {numbers}")

    # Insert in the middle: elements from that index onward shift right.
    middle = len(numbers) // 2
    insert_at(numbers, middle, 25)
    print(f"After insert in the middle (index {middle}, value 25): {numbers}")

    # Insert at the end: no shifting of existing elements is required.
    insert_at(numbers, len(numbers), 50)
    print(f"After insert at the end (value 50): {numbers}")

    # ===============================
    # DELETION TESTS
    # ===============================
    # Delete from the beginning, middle, and end. Show the removed value
    # and the list after each removal so the shift is visible.

    print("\n=== DELETION TESTS ===")
    print(f"List before deletions: {numbers}")

    # Delete at the beginning: remaining elements shift one index left.
    removed = delete_at(numbers, 0)
    print(f"Removed from beginning: {removed}")
    print(f"  List now: {numbers}")

    # Delete in the middle: elements after that index shift left to close the gap.
    middle = len(numbers) // 2
    removed = delete_at(numbers, middle)
    print(f"Removed from middle (index {middle}): {removed}")
    print(f"  List now: {numbers}")

    # Delete at the end: no remaining elements need to shift.
    removed = delete_at(numbers, len(numbers) - 1)
    print(f"Removed from end: {removed}")
    print(f"  List now: {numbers}")

    # ===============================
    # SEARCH TESTS
    # ===============================
    # Search for a value that exists and one that does not.

    print("\n=== SEARCH TESTS ===")
    print(f"Searching in: {numbers}")

    # Existing value: linear scan finds it and returns its index.
    found_index = search_value(numbers, 20)
    print(f"Search for 20 (exists): index {found_index}")

    # Missing value: the scan reaches the end and returns -1.
    missing_index = search_value(numbers, 99)
    print(f"Search for 99 (does not exist): {missing_index}")

    # ===============================
    # EDGE CASES
    # ===============================
    # Invalid delete index, delete from an empty list, and insert into
    # an empty list. Search for a missing value is also shown above.

    print("\n=== EDGE CASES ===")

    # Invalid index: out of range, so delete_at returns None instead of crashing.
    invalid = delete_at(numbers, 100)
    print(f"Delete at invalid index 100: {invalid} (expected None)")
    print(f"  List unchanged: {numbers}")

    # Delete from an empty list: there is no valid index, so return None.
    empty = []
    empty_delete = delete_at(empty, 0)
    print(f"Delete from empty list at index 0: {empty_delete} (expected None)")

    # Insert into an empty list: the new value becomes the only element.
    insert_at(empty, 0, "first")
    print(f"Insert into empty list: {empty}")

    demonstrate_real_world()


if __name__ == "__main__":
    main()
