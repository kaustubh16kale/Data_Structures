class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def update(self, data, new_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                current_node.data = new_data
                break
            current_node = current_node.next

    def delete(self, data):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next
    
    def remove(self, data):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node.next = current_node.next
                break
            previous_node = current_node
            current_node = current_node.next

def main():
    linked_list = LinkedList()
    while True:
        print("1) Insert in list\n2) Update list\n3) Delete from list\n4) Remove from list\n5) Print list\n6) Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the value to insert: ")
            linked_list.insert(data)
        elif choice == 2:
            data = input("Enter the value to update: ")
            new_data = input("Enter the new value: ")
            linked_list.update(data, new_data)
        elif choice == 3:
            data = input("Enter the value to delete: ")
            linked_list.delete(data)
        elif choice == 4:
            data = input("Enter the value to remove: ")
            linked_list.remove(data)
        elif choice == 5:
            current_node = linked_list.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
            print()  # For newline
        elif choice == 6:
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
