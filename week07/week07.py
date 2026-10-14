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


pokemons = LinkedList()
pokemons.append('꼬부기')
pokemons.append('피카츄')
pokemons.append('파이리')
# print(pokemons.head.data)
# print(pokemons.head.next.data)
# print(pokemons.head.next.next.data)
print(pokemons)