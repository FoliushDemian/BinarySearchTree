class Transistor:
    def __init__(self, type_of_transistor: str, brand: str, max_current: float, max_voltage: float):
        self.type_of_transistor = type_of_transistor
        self.brand = brand
        self.max_current = max_current
        self.max_voltage = max_voltage

    def __str__(self):
        return f'{self.type_of_transistor}, {self.brand}, {self.max_current}, {self.max_voltage}'


class TreeNode:

    def __init__(self, transistor: Transistor):
        self.left = None
        self.right = None
        self.parent = None
        self.transistor = transistor

    def find_node(self, type_to_delete: str):  # шукаєм вказівник на ноду в якій є потрібний транзистор
        if self.transistor.type_of_transistor == type_to_delete:
            return self  # повертає силку на самого себе
        left_result = None
        right_result = None
        if self.left:  # то саме шо self.left is not None
            left_result = self.left.find_node(type_to_delete)
        if self.right:
            right_result = self.right.find_node(type_to_delete)
        return left_result if left_result else right_result

    def print_if_max_current_and_max_voltage_are(self, max_current, max_voltage):
        if self.left:
            self.left.print_if_max_current_and_max_voltage_are(max_current, max_voltage)
        if self.right:
            self.right.print_if_max_current_and_max_voltage_are(max_current, max_voltage)
        if self.transistor.max_current == max_current and self.transistor.max_voltage == max_voltage:
            print(self.transistor)

    def print_nodes(self):
        if self.left:
            self.left.print_nodes()
        if self.right:
            self.right.print_nodes()
        print(self.transistor)


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

    def find(self, type_to_delete: str):
        if self.root:
            if self.root.transistor.type_of_transistor == type_to_delete:
                return self.root
            else:
                return self.root.find_node(type_to_delete)
        else:
            return None

    def delete_nodes_with_type(self, type_to_delete: str):
        node_to_delete = self.find(type_to_delete)
        if node_to_delete:
            while node_to_delete.parent is None:
                if node_to_delete.left:
                    if node_to_delete.right:
                        self.root = node_to_delete.right
                        self.root.parent = None
                        current_node = node_to_delete.right
                        while current_node.left:
                            current_node = current_node.left
                        current_node.left = node_to_delete.left
                        node_to_delete.left.parent = current_node
                    else:
                        self.root = node_to_delete.left
                        self.root.parent = None
                else:
                    if node_to_delete.right:
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
            else:
                node_to_delete.parent.right = node_to_delete.right
                if node_to_delete.right:
                    node_to_delete.right.parent = node_to_delete.parent
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
        if self.root.left:
            self.root.left.print_if_max_current_and_max_voltage_are(max_current, max_voltage)
        if self.root.right:
            self.root.right.print_if_max_current_and_max_voltage_are(max_current, max_voltage)
        if self.root.transistor.max_current == max_current and self.root.transistor.max_voltage == max_voltage:
            print(self.root.transistor)

    def print_binary_search_tree(self):
        if self.root.left:
            self.root.left.print_nodes()
        if self.root.right:
            self.root.right.print_nodes()
        print(self.root.transistor)
