from __future__ import annotations


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_start(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            active = self.head
            while active.next:
                active = active.next
            active.next = node

    @staticmethod
    def insert_after(prev_node: Node, data: Node | int):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        if isinstance(data, int):
            data = Node(data)
        data.next = prev_node.next
        prev_node.next = data

    def delete_node(self, key: int):
        active = self.head
        if active and active.data == key:
            self.head = active.next
            del active
            return
        prev = None
        while active and active.data != key:
            prev = active
            active = active.next
        if active is None:
            return
        prev.next = active.next
        del active

    def search_element(self, data):
        active = self.head
        while active:
            if active.data == data:
                return active
            active = active.next
        return

    def print_list(self):
        active = self.head
        while active:
            print(active.data, end=" ")
            active = active.next
        print()

    def reverse(self):
        active = self.head
        previous = None

        while active:
            next_node = active.next
            active.next = previous
            previous = active
            active = next_node
        self.head = previous

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return

        sorted_head = None
        current = self.head

        while current is not None:
            next_node = current.next

            if sorted_head is None or sorted_head.data > current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next is not None and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current

            current = next_node

        self.head = sorted_head

    def merge_sorted_lists(self, other: LinkedList):
        merged_list = LinkedList()
        self_active = self.head
        other_active = other.head

        while self_active is not None and other_active is not None:
            if self_active.data < other_active.data:
                merged_list.insert_end(self_active.data)
                self_active = self_active.next
            else:
                merged_list.insert_end(other_active.data)
                other_active = other_active.next

        while self_active:
            merged_list.insert_end(self_active.data)
            self_active = self_active.next

        while other_active:
            merged_list.insert_end(other_active.data)
            other_active = other_active.next

        self.head = merged_list.head


def main():
    ls = LinkedList()

    numbers = (-2, -3, -5, 0, 3, 7, 9, 14, 19, 23, 28)
    for data in numbers:
        if data % 2:
            ls.insert_start(data)
        else:
            ls.insert_end(data)
    ls.print_list()

    ls.insert_end(6)
    ls.insert_end(13)
    ls.print_list()

    ls.insert_after(ls.search_element(3), -13)
    ls.print_list()

    ls.delete_node(7)
    ls.print_list()

    print(f"Search for 13: {'Found' if ls.search_element(13) else 'Not found'}")

    ls.reverse()
    ls.print_list()

    ls.insertion_sort()
    ls.print_list()

    ls_2 = LinkedList()

    ls_2.insert_end(2)
    ls_2.insert_end(5)
    ls_2.insert_end(7)
    ls_2.insert_end(-1)
    ls_2.insert_end(33)
    ls_2.insertion_sort()
    ls_2.print_list()

    ls.merge_sorted_lists(ls_2)
    ls.print_list()


if __name__ == "__main__":
    main()
