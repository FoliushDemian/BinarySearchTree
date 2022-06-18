from binary_search_tree import BinarySearchTree
from transistor import Transistor

if __name__ == '__main__':
    Tree1 = BinarySearchTree()
    Tree1.insert(Transistor("pnp", "kt1", 100, 5))
    Tree1.insert(Transistor("pnp", "kt2", 50, 5))
    Tree1.insert(Transistor("pnp", "kt3", 150, 5))
    Tree1.insert(Transistor("pnp", "lol69", 25, 5))
    Tree1.insert(Transistor("npn", "R2D2", 75, 5))
    Tree1.insert(Transistor("pnp", "gg2", 175, 5))
    Tree1.insert(Transistor("pnp", "17MB", 125, 5))
    Tree1.delete_nodes_with_type("pnp")

    Tree1.print_if_max_current_and_max_voltage_are(100, 5)

    Tree1.print_binary_search_tree()

