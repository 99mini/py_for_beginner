# node class
class Node:
    def __init__(self, element) -> None:
        self.element = element
        self.next = None
        self.previous = None

# 양방향 연결 리스트
class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = Node('head')
    
    def find(self, item):
        curr_node = self.head
        while curr_node.element != item:
            curr_node = curr_node.next
        return curr_node

    def insert(self, item, new):
        new_node = Node(new)
        curr_node = self.find(item)
        new_node.next = curr_node.next
        curr_node.next = new_node
        new_node.previous = curr_node

    def show(self):
        curr_node = self.head
        while curr_node.next is not None:
            print(curr_node.element, end=' -> ')
            curr_node = curr_node.next
        print(curr_node.element)

    def remove(self,item):
        curr_node = self.find(item)

        curr_node.previous.next = curr_node.next
        curr_node.previous = None

        if curr_node.next is not None:
            curr_node.next.previous = curr_node.previous
            curr_node.next = None

    def find_last(self):
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        return curr_node

    def show_reverse(self):
        curr_node = self.find_last()
        while curr_node.previous is not None:
            print(curr_node.element, end=' <- ')
            curr_node = curr_node.previous
        print(curr_node.element)

double_linked_list = DoubleLinkedList()
double_linked_list.insert('head','1')
double_linked_list.insert('1','2')
double_linked_list.insert('2','3')
double_linked_list.insert('3','4')
double_linked_list.show()
double_linked_list.remove('4')
double_linked_list.show()
print(double_linked_list.find_last().element)
double_linked_list.show_reverse()