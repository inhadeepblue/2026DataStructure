from encodings import search_function


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            raise IndexError('스택이 비어 있습니다. 삭제 불가!')
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data


subjects = Stack()
subjects.push("자료구조")
subjects.push("웹프로그래밍")
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())