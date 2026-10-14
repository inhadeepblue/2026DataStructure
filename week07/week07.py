class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        """
        연결 리스트 초기화 함수
        """
        self.head = None


    def append(self, data):
        """
        노드 추가 함수
        :param data: 노드 데이터 값
        :return: None
        """
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)


ll = LinkedList()
ll.append('꼬부기')
ll.append('피카츄')
ll.append('파이리')
# print(ll.head.data)
# print(ll.head.next.data)
print(ll.head.next.next.data)