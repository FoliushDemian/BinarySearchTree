from transistor import Transistor


class TreeNode:

    def __init__(self, transistor: Transistor):
        self.left = None
        self.right = None
        self.parent = None
        self.transistor = transistor

    def find_node(self, type_to_delete: str):  # шукаєм вказівник на ноду в якій є потрібний транзистор
        if self.transistor.type_of_transistor == type_to_delete:
            return self  # повертає силку на самого себе
        left_result = None  # це будуть посилання
        right_result = None
        if self.left:  # то саме шо self.left is not None
            left_result = self.left.find_node(type_to_delete)
        if self.right:
            right_result = self.right.find_node(type_to_delete)
        return left_result if left_result else right_result

    def print_if_max_current_and_max_voltage_are(self, max_current, max_voltage):
        if self.left: # це нода
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
