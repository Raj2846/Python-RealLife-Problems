from dataclasses import dataclass

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
        
class BST:
    def __init__(self):
        self.root =None
        
    def insert(self,data):
        self.root= self._insert(self.root,data)
        
    #a leading underscore signals "this is internal/private — not meant to be called from outside the class.
    def _insert(self,node,data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left= self._insert(node.left,data)
        elif data > node.data :
            node.right= self._insert(node.right,data)
            
        return node
    
    def search(self,target):
        return self._search(self.root,target)
    
    def _search(self,node,target):
        if node is None:
            return False
        if target == node.data:
            return True
        elif target < node.data:
            return self._search(node.left,target)
        else:
            return self._search(node.right,target)
        
    def delete(self,target):
        self.root= self._delete(self.root,target)
        
    def _delete(self,node,target):
        if node is None:
            return None
        
        if target < node.data:
            node.left = self._delete(node.left,target)
        elif target > node.data:    
            node.right = self._delete(node.right,target)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor= self._min_value_node(node.right)
            node.data=successor.data
            node.right= self._delete(node.right,successor.data)
            
        return node
    
    def _min_value_node(self,node):
        current=node
        while current.left is not None:
            current=current.left
        return current            
    
    def inorder(self):
        result=[]
        self._inorder(self.root,result)
        return result
    
    def _inorder(self,node,result:list):
        if node:
            self._inorder(node.left,result)
            result.append(node.data)
            self._inorder(node.right,result)
            
            
            
if __name__ == "__main__":
    bst = BST()
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)

    print("Inorder traversal:", bst.inorder())   # sorted order
    print("Search 40:", bst.search(40))           # True
    print("Search 100:", bst.search(100))         # False

    bst.delete(30)
    print("After deleting 30:", bst.inorder())