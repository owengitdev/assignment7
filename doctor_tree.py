class DoctorNode:
    def __init__(self,doctor):
        self.doctor = doctor
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None
        
    def preorder(self, node):
        if node is None:
            return []
        result = [node.value]

        result += self.preorder(node.left)
        result += self.preorder(node.right)

        return result

    def inorder(self, node):
        if node is None:
            return []
        result = []
        result += self.preorder(node.left)
        result.append(node.value)
        result += self.preorder(node.right)

        return result

    def postorder(self, node):
        if node is None:
            return []
        result = []
        result += self.preorder(node.left)
        result += self.preorder(node.right)
        result.append(node.value)

        return result

    def insert(self, doctor, side, current_node=None):
        if self.root is None:
            print("Tree is empty.")
            return None

        if current_node is None:
            current_node = self.root

        if current_node.value == doctor:

            if side == "left" and current_node.left is None:
                current_node.left = DoctorNode(doctor)
                print(f"{doctor} added under {doctor} on the right")
                return True
            elif side == "right" and current_node.right is None:
                current_node.right = DoctorNode(doctor)
                print(f"{doctor} added under {doctor} on the right.")
                return True
            else:
                print(f"{doctor} already has a {side} subordinate.")
                return True

        found_left = False
        found_right = False

        if current_node.left:
            found_left = self.insert(doctor, side)
        if current_node.right and not found_left:
            found_right = self.insert(doctor, side)

        if not(found_left or found_right):

          if current_node == self.root:
            print(f"Manager node {doctor} not found in the tree")
          return False
        return True

# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft")
print(DoctorTree())

