from transistor import Transistor
from tree_node import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, transistor: Transistor):
        if self.root is None:
            self.root = TreeNode(transistor)
            self.root.parent = None
        else:
            current_node = self.root
            while True:
                if transistor.max_current < current_node.transistor.max_current:
                    if current_node.left is None:
                        current_node.left = TreeNode(transistor)
                        current_node.left.parent = current_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = TreeNode(transistor)
                        current_node.right.parent = current_node
                        break
                    else:
                        current_node = current_node.right

    def find(self, type_to_delete: str):  # ми не можем запхати в find_node бо корінь треба перевіряти окремо
        if self.root:
            return self.root.find_node(type_to_delete)
        else:
            return None

    def delete_nodes_with_type(self, type_to_delete: str):
        node_to_delete = self.find(type_to_delete)
        if node_to_delete:  # окремо для видалення кореня
            while node_to_delete.parent is None:
                if node_to_delete.left:
                    if node_to_delete.right:
                        self.root = node_to_delete.right # вказує на 150
                        self.root.parent = None # батько 150 None
                        current_node = node_to_delete.right
                        while current_node.left:
                            current_node = current_node.left
                        current_node.left = node_to_delete.left
                        node_to_delete.left.parent = current_node
                    else:
                        self.root = node_to_delete.left
                        self.root.parent = None
                elif node_to_delete.right:
                    self.root = node_to_delete.right
                    self.root.parent = None
                else:
                    self.root = None
                node_to_delete = self.find(type_to_delete)
                if node_to_delete is None:
                    break

        while node_to_delete:
            if node_to_delete == node_to_delete.parent.left:
                if node_to_delete.right:
                    node_to_delete.parent.left = node_to_delete.right
                    node_to_delete.right.parent = node_to_delete.parent
                    if node_to_delete.left:
                        current_node = node_to_delete.right
                        while current_node.left:
                            current_node = current_node.left
                        current_node.left = node_to_delete.left
                        node_to_delete.left.parent = current_node
                elif node_to_delete.left:
                    node_to_delete.parent.left = node_to_delete.left
                    node_to_delete.left.parent = node_to_delete.parent
                else:
                    node_to_delete.parent.left = None
            elif node_to_delete.right:
                node_to_delete.parent.right = node_to_delete.right
                node_to_delete.right.parent = node_to_delete.parent
                if node_to_delete.left:
                    current_node = node_to_delete.right
                    while current_node.left:
                        current_node = current_node.left
                        node_to_delete.left.parent = current_node
                    current_node.left = node_to_delete.left
            elif node_to_delete.left:
                node_to_delete.parent.right = node_to_delete.left
                node_to_delete.left.parent = node_to_delete.parent
            else:
                node_to_delete.parent.right = None
            node_to_delete = self.find(type_to_delete)

    def print_if_max_current_and_max_voltage_are(self, max_current: float, max_voltage: float):
        if self.root:
            if self.root.left:
                self.root.left.print_if_max_current_and_max_voltage_are(max_current, max_voltage) # то не рекурсія просто
            if self.root.right:                                                                   # назви однакові
                self.root.right.print_if_max_current_and_max_voltage_are(max_current, max_voltage)
            if self.root.transistor.max_current == max_current and self.root.transistor.max_voltage == max_voltage:
                print(self.root.transistor)

    def print_binary_search_tree(self):
        if self.root:
            if self.root.left:
                self.root.left.print_nodes()
            if self.root.right:
                self.root.right.print_nodes()
            print(self.root.transistor)
