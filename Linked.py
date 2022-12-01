class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def adiciona(self, data):

        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next != None:
            current_node = current_node.next

        current_node.next = new_node
        return

    def tamanho(self):

        if self.head == None:
            return 0

        current_node = self.head
        total = 0

        while current_node.next != None:
            current_node = current_node.next
            total += 1
        return total

    def imprime(self):

        contents = self.head

        if contents == None:
            print("A lista está vazia")
            return

        while contents != None:
            print(contents.data)
            contents = contents.next

        print("--------------")
        return
