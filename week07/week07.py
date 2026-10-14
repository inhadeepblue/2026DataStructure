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
        if not self.head:  # 최초 노드 연결용. 단 1회 실행
            self.head = Node(data)
            return
        current = self.head  # 첫 번째 노드의 위치를 받은 지역변수 current
        while current.next:  # 가르키는 다음 노드가 존재하면 반복.
            current = current.next  # current를 다음 노드로 이동
        current.next = Node(data)  # while문 종료(마지막 노드를 찾음) 후 새 노드 생성. 그리고 새 노드를 마지막 노드에 연결.


    def __str__(self):  # 매직메서드로 print 함수등에 출력할 내용을 정리
        n = self.head
        while n is not None:
            print(n.data)
            n = n.next  # 다음 노드로 이동
        return '[끝]'


pokemons = LinkedList()
pokemons.append('꼬부기')  # head
pokemons.append('피카츄')
pokemons.append('파이리')
pokemons.append('뮤')
print(pokemons)  # <__main__.LinkedList object at 0x000002BDD72C7230>