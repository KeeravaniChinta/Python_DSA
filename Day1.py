class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add_node(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=node
    def delete(self,data):
        if self.head.data==data:
            self.head=None
        else:
            current=self.head
            while current.next is not None:
                if current.next.data==data:
                    current.next=current.next.next
                    print("Deleted")
                    return
                current=current.next
            print("Not Found")
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,"->",end=" ")
            current=current.next
        print("None")
    def insert_at_beginning(self,data):
        node=Node(data)
        if not self.head:
            self.head=node
        else:
            node.next=self.head
            self.head=node

# ll1=LinkedList()
# ll1.add_node(10)
# ll1.add_node(20)
# ll1.add_node(30)
# ll1.add_node(40)
# ll1.add_node(50)
# ll1.display()
