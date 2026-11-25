class Stack:
    def __init__(self):
        self.items = list()   # self.items = []

    def push(self, item):
        """
        스택에 원소를 추가(삽입)하는 함수
        :param item: 문자열, 정수, 실수 등등
        :return: None
        """
        self.items.append(item)

    def pop(self):
        """
        스택의 마지막 원소(top이 가리키고 있는) 리턴하고 삭제하는 함수
        :return: items 리스트의 맨 마지막 원소
        """
        return self.items.pop()

    def peek(self):
        """
        스택의 마지막 원소를 리턴 (삭제 안함)
        역방향 인덱싱 또는 정방향 인덱싱 가능
        :return:
        """
        return self.items[-1]  # 역방향
        #return self.items[len(self.items)-1]  # 정방향

    def is_empty(self):
        """
        스택이 비어 있는지 확인
        :return: 스택에 원소가 없으면 True 스택에 원소가 한개 이상 존재하면 False
        """
        return len(self.items) == 0

    def size(self):
        """
        스택에 원소가 몇 개 인지 리턴
        :return: 스택 원소 개수(정수)
        """
        return len(self.items)

subjects = Stack()
artists = Stack()
artists.push("핑클")
subjects.push("웹프로그래밍")
subjects.push("자료구조")
artists.push("SES")
print(subjects.pop())
print(subjects.peek())  # top 원소 확인
print(artists.peek())
print(artists.size())
print(subjects.size())
print(artists.is_empty())
#help(Stack.pop)
help(Stack)  # Docstring