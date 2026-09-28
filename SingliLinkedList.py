class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        self.head
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next

        current.next=new_node
    def append_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def append_after_value(self,data,target):
        new_node=Node(data)
        current=self.head
        while current is not None:
            if current.data == target:
                new_node.next=current.next
                current.next=new_node
                return
            current=current.next
        print(f"{target} not found")
    def search(self,data):
        current=self.head
        while current is not None:
            if current.data==data:
                return True
            current=current.next
        return False
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
        print(current)
    def delete_beg(self):
        if self.head is None:
            print("empty list")
        self.head=self.head.next
    def update(self,value,data):
        current=self.head
        while current is not None:
            if current.data==value:
                current.data=data
                break
            current=current.next
ll=LinkedList()
ll.append(18)
ll.append(45)
ll.append_beg(33)
ll.append_beg(93)
ll.append_after_value(7,18)
ll.search(33)
ll.delete_beg()
ll.update(7,18)
ll.display()