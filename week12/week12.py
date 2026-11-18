class Stack:
    def __init__(self):
        self.items = list()   # self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        #return self.items[-1]
        return self.items[len(self.items)-1]

subjects = Stack()
artists = Stack()
artists.push("핑클")
subjects.push("웹프로그래밍")
subjects.push("자료구조")
artists.push("SES")
print(subjects.pop())
print(subjects.peek())  # top 원소 확인
print(artists.peek())
