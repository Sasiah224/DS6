class EmployeeNode:
    """Represents an employee and their direct reports."""

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    """Manages the employee reporting structure."""

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        first_call = current_node is None

        if first_call:
            current_node = self.root

            if current_node is None:
                print("Add a team lead first.")
                return False

            if side not in ("left", "right"):
                print("Please choose 'left' or 'right'.")
                return False

        # Check whether this employee is the requested manager.
        if current_node.name == manager_name:
            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the left of {manager_name}.")
                else:
                    print("This manager already has a left report.")

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the right of {manager_name}.")
                else:
                    print("This manager already has a right report.")

            return True

        # Recursively search the left branch.
        if current_node.left is not None:
            found = self.insert(
                manager_name, employee_name, side, current_node.left
            )
            if found:
                return True

        # Recursively search the right branch.
        if current_node.right is not None:
            found = self.insert(
                manager_name, employee_name, side, current_node.right
            )
            if found:
                return True

        if first_call:
            print(f"Manager '{manager_name}' was not found.")

        return False

    def print_tree(self, node=None, level=0):
        if node is None and level == 0:
            node = self.root

            if node is None:
                print("The team directory is empty.")
                return

        if node is None:
            return

        print("    " * level + "- " + node.name)

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here









# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    company_directory()


    