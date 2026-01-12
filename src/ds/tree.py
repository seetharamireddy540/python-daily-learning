
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def hight(root) -> bool:
    is_balanced: bool = True

    def check_balance(node: Node) -> int:
        nonlocal is_balanced
        if node is None:
            return 0
        left_height = check_balance(node.left)
        right_height = check_balance(node.right)
        if abs(left_height - right_height) > 1:
            is_balanced = False
        return max(left_height, right_height) + 1

    check_balance(root)
    return is_balanced


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    print(hight(root))
