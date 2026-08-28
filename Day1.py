# #singly linked list
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedList:
#     def __init__(self):
#         self.head=None
#     def add_node(self,data):
#         node=Node(data)
#         if not self.head:
#             self.head=node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=node
#     def delete(self,data):
#         if self.head.data==data:
#             self.head=self.head.next
#         else:
#             current=self.head
#             while current.next is not None:
#                 if current.next.data==data:
#                     current.next=current.next.next
#                     print("Deleted")
#                     return
#                 current=current.next
#             print("Not Found")
#     def display(self):
#         current=self.head
#         while current is not None:
#             print(current.data,"->",end=" ")
#             current=current.next
#         print("None")
#     def insert_at_beginning(self,data):
#         node=Node(data)
#         if not self.head:
#             self.head=node
#         else:
#             node.next=self.head
#             self.head=node
#     def insert_at_kth_position(self,data,k):
#         node=Node(data)
#         if not self.head:
#             self.head=node
#         else:
#             current=self.head
#             count=1
#             while current is not None and k>1:
#                 current=current.next
#                 count+=1
#                 if count==k-1:
#                     node.next=current.next
#                     current.next=node
#                     print("Inserted at kth position")
#                     return
#             print("Not Found")
#     def reverse(self):
#         prev = None
#         current = head
#         while current:
#             next_node = current.next
#             current.next = prev
#             prev = current
#             current = next_node
#         self.head=prev

# # ll1=LinkedList()
# # ll1.add_node(10)
# # ll1.add_node(20)
# # ll1.add_node(30)
# # ll1.add_node(40)
# # ll1.add_node(50)
# # ll1.display()


# #doubly linked list
# class DNode:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
#         self.prev=None
# class DLinkedList:
#     def __init__(self):
#         self.head=None
#     def add_node(self,data):
#         node=DNode(data)
#         if self.head is None:
#             self.head=node
#         else:
#             current=self.head
#             while current.next is not None:
#                 current=current.next
#             current.next=node
#             node.prev=current
#     def delete(self,data):
#         if self.head is None:
#             print("Not Found")
#             return
#         current=self.head
#         while current is not None:
#             if current.data==data:
#                 if current.prev is None:
#                     self.head=current.next
#                     if self.head:
#                         self.head.prev=None
#                 else:
#                     current.prev.next=current.next
#                     if current.next:
#                         current.next.prev=current.prev
#                 print("Deleted")
#                 return
#             current=current.next
#         print("Not Found")
#     def display(self):
#         current=self.head
#         while current is not None:
#             print(current.data,"<->",end=" ")
#             current=current.next
#         print("None")
# dll=DLinkedList()
# dll.add_node(10)
# dll.add_node(20)
# dll.add_node(30)
# dll.add_node(40)
# dll.display()
# dll.delete(30)
# dll.display()


# # Circular Linked List
# class CNode:
#     def __init__(self, data):
#         self.data=data
#         self.next=None
# class CircularLinkedList:
#     def __init__(self):
#         self.head=None
#     def add_node(self,data):
#         node=CNode(data)
#         if not self.head:
#             self.head=node
#             node.next=self.head
#         else:
#             current=self.head
#             while current.next!=self.head:
#                 current=current.next
#             current.next=node
#             node.next=self.head
#     def delete(self,data):
#         if not self.head:
#             print("Not Found")
#             return
#         if self.head.data==data:
#             if self.head.next==self.head:
#                 self.head=None
#             else:
#                 current=self.head
#                 while current.next!=self.head:
#                     current=current.next
#                 self.head=self.head.next
#                 current.next=self.head
#             print("Deleted")
#             return
#         current=self.head
#         while current.next!=self.head:
#             if current.next.data==data:
#                 current.next=current.next.next
#                 print("Deleted")
#                 return
#             current=current.next
#         print("Not Found")
#     def display(self):
#         if self.head is None:
#             print("Empty List")
#             return
#         current=self.head
#         while True:
#             print(current.data,"->",end=" ")
#             current=current.next
#             if current==self.head:
#                 break
#         print("(Head)")
# cll = CircularLinkedList()
# cll.add_node(10)
# cll.add_node(20)
# cll.add_node(30)
# cll.add_node(40-)
# cll.display()
# cll.delete(30)
# cll.display()


# #Trees
# class TreeNode:
#     def ___init__(self,data):
#         self.data=data
#         self.children=[]
# tnode1=TreeNode(1)
# tnode1=TreeNode(2)
# tnode1.children.append(tnode2)
# print(tnode1.data)
# print(tnode1.children[0].data)
# class Tree:
#     def __init__(self):
#         self.root=None
#     def add_node(self,data,parent_data=None):
#         new_node=TreeNode(data)
#         if not self.root:
#             self.root=new_node
#             return
#         if parent_data:
#             parent_node=self.findParent(parent_data,self.root)
#         if parent_node:
#             parent_node.children.append(new_node)
#     def findParent(self,data,node):
#         current_node=node
#         if current_node.data==data:
#             return current_node
#         for child in current_node.children:
#             NodeFound=self.findParent(child,data)
#             if NodeFound:
#                 return NodeFound
#         return None
#     def display(self,node=None,depth=0):
#         if node is None:
#             node=self.root
#         current_node=node
#         print("-"*depth+str(current_node.data))
#         for child in current_node.children:
#             self.display(child,depth+1) 


# #Binary Tree
# class BinaryNode:
#     def __init__ (self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def addNode(self,data):
#         new_node=BinaryNode(data)
#         if not self.root:
#             self.root=new_node
#             return
#         self.recursiveAdd(new_node,self.root)
#     def recursiveAdd(self,node,current_node):
#         if current_node.left is None:
#             current_node.left=node
#         elif current_node.right is None:
#             current_node.right=node
#         else:
#             self.recursiveAdd(node,current_node.left)
#     def display(self,node=None,depth=0):
#         if node is None:
#             node=self.root
#         current_node=node
#         print("-"*depth+str(current_node.data))
#         if node.left:
#             self.display(node.left, depth + 1)
#         if node.right:
#             self.display(node.right, depth + 1)
# tree = BinaryNode()
# tree.addNode(50)
# tree.addNode(30)
# tree.addNode(70)
# tree.addNode(20)
# tree.addNode(40)
# tree.addNode(60)
# tree.addNode(80)
# tree.display()



#Binary search tree(nodes are unique)
class BinarySearchNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def addNode(self,data):
            new_node=BinarySearchNode(data)
            if not self.root:
                self.root=new_node
                return
            self.recursiveAdd(new_node,self.root)
    def recursiveAdd(self,node,current_node):
        if node.data<current_node.data:
            if current_node.left is None:
                current_node.left=node
                return 
            else:
                self.recursiveAdd(node,current_node.left)
        elif node.data>current_node.data:
            if current_node.right is None:
                current_node.right=node
                return 
            else:
                self.recursiveAdd(node,current_node.right)
    def display(self,node=None,depth=0):
        if node is None:
            node=self.root
        current_node=node
        print("-"*depth+str(current_node.data))
        if current_node.left:
            self.display(current_node.left,depth+1)
        if current_node.right:
            self.display(current_node.right,depth+1)
    def findMin(self,node):  
        current_node=node
        while current_node.left is not None:
            current_node=current_node.left
        return current_node
    def findMax(self,node):
        current_node=node
        while current_node.right is not None:
            current_node=current_node.right
        return current_node