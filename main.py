class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max_value(root):
    if root is None:
        return None
    
    while root.right:
        root = root.right

    return root.key

# Приклад використання:
# Створення дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Знаходження максимального значення
max_value = find_max_value(root)
print(f"Найбільше значення у дереві: {max_value}")


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min_value(root):
    if root is None:
        return None
    
    while root.left:
        root = root.left

    return root.key

# Приклад використання:
# Створення дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Знаходження мінімального значення
min_value = find_min_value(root)
print(f"Найменше значення у дереві: {min_value}")

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    else:
        return root.key + tree_sum(root.left) + tree_sum(root.right)

# Приклад використання:
# Створення дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Знаходження суми всіх значень
total_sum = tree_sum(root)
print(f"Сума всіх значень у дереві: {total_sum}")