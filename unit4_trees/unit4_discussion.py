"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and start with no children.
        # Left and right stay None until insert() attaches a subtree.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty tree has no root. The first insert() creates it.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST using the recursive helper.

        Insertion depends on comparing the new value to the current node:
        smaller values go left, larger values go right. That ordering is
        what later lets search skip an entire subtree at each step.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Recursive BST insertion.

        When node is None, this path has reached an empty child slot,
        so a new Node is created there. Smaller values walk left;
        larger values walk right. Duplicates are sent right so every
        insert still produces a valid BST (no extra duplicate policy).
        """
        # Empty slot found: create the new node and return it so the
        # parent can attach it as left or right.
        if node is None:
            return Node(value)

        # Smaller than the current node: the value belongs in the left
        # subtree, so only that side needs to grow.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        # Larger (or equal): belong in the right subtree.
        else:
            node.right = self._insert_recursive(node.right, value)

        # Return this node so parent links stay correct after recursion.
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Returns True if found, False if not.

        BST search is often more efficient than linear search because
        each comparison discards one entire subtree. In a reasonably
        balanced tree the remaining work is about half of the nodes
        at every step (O(log n)), instead of checking every element
        in order (O(n)).
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Recursive BST search: go left, go right, or stop."""
        # Reached an empty child, or the tree itself is empty.
        if node is None:
            return False
        if value == node.value:
            return True
        # Target is smaller, so it cannot be in the right subtree.
        if value < node.value:
            return self._search_recursive(node.left, value)
        # Target is larger, so it cannot be in the left subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """Return a list of values from an in-order traversal."""
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        In-order traversal: left subtree, current node, right subtree.

        In a BST, every value in the left subtree is smaller than the
        current node, and every value in the right subtree is larger.
        Visiting left, then node, then right therefore walks the keys
        from smallest to largest and produces sorted output.
        """
        if node is None:
            return
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def demonstrate_real_world():
    """
    Real-world scenario: a campus ID lookup.

    Student IDs are stored in a BST so staff can check whether an ID
    is enrolled without scanning every record. Insert keeps IDs ordered;
    search walks left or right; in-order prints IDs from low to high.
    """
    print("\n=== REAL-WORLD SCENARIO: CAMPUS ID LOOKUP ===")
    print("Student IDs are stored in a BST. Each comparison drops")
    print("the half of the directory that cannot contain the ID.")

    directory = BST()
    enrolled_ids = [4521, 2108, 7803, 3310, 6104, 1550, 9002]
    print(f"\nEnrolling IDs: {enrolled_ids}")
    for student_id in enrolled_ids:
        directory.insert(student_id)

    print(f"Directory in order (in-order traversal): {directory.inorder()}")

    # An ID that exists: search walks toward that leaf/internal node.
    print(f"Lookup 3310 (enrolled): {directory.search(3310)}")
    # An ID that does not exist: search ends at a None child.
    print(f"Lookup 9999 (not enrolled): {directory.search(9999)}")


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    # Create a BST and insert at least 7 values. The first value
    # becomes the root. Later values go left if smaller than the
    # current node and right if larger. That split is why a BST
    # shrinks the remaining search space at each step: after one
    # comparison, an entire subtree can be ignored.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values = [50, 30, 70, 20, 40, 60, 80, 25]
    print(f"Inserting values: {values}")
    print("50 is the root. 30 and 20/40/25 go left of 50;")
    print("70 and 60/80 go right of 50.")
    for value in values:
        tree.insert(value)
        print(f"  Inserted {value}")
    print(f"Tree now holds {len(values)} values.")

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    # Left, node, right visits keys from smallest to largest because
    # the BST already stores smaller values on the left.

    print("\n=== IN-ORDER TRAVERSAL ===")
    sorted_values = tree.inorder()
    print(f"In-order result: {sorted_values}")
    print("This list is sorted without a separate sort step.")
    print("Left subtree values are always smaller than the node;")
    print("right subtree values are always larger.")

    # ===============================
    # SEARCH TESTS
    # ===============================
    # Existing values should return True. Missing values walk until
    # a None child and return False.

    print("\n=== SEARCH TESTS ===")
    print("Existing values (should be True):")
    print(f"  search(40): {tree.search(40)}")
    print(f"  search(80): {tree.search(80)}")
    print("Missing values (should be False):")
    print(f"  search(15): {tree.search(15)}")
    print(f"  search(99): {tree.search(99)}")

    # ===============================
    # EDGE CASES
    # ===============================
    # Empty tree, a one-node tree, and a duplicate insert.

    print("\n=== EDGE CASES ===")

    # Empty tree: there is no root, so traversal is empty and search fails.
    empty_tree = BST()
    print(f"In-order on empty tree: {empty_tree.inorder()} (expected [])")
    print(f"Search 10 on empty tree: {empty_tree.search(10)} (expected False)")

    # Single node: insert one value; search finds it; in-order is that value.
    single = BST()
    single.insert(42)
    print(f"One-node tree in-order: {single.inorder()}")
    print(f"Search 42 in one-node tree: {single.search(42)}")
    print(f"Search 7 in one-node tree: {single.search(7)}")

    # Duplicate: this BST sends equals to the right, so 50 appears twice.
    tree.insert(50)
    print(f"After inserting duplicate 50, in-order: {tree.inorder()}")
    print("Duplicates are allowed and stored on the right of the match.")

    demonstrate_real_world()


if __name__ == "__main__":
    main()
