import random


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


    def search(self, target):
        """
        노드 검색 함수
        :param target: 찾고자 하는 노드 데이터 값
        :return: True or False
        """
        current = self.head
        while current.next:
            if current.data == target:
                return True  # 찾고자 하는 노드를 찾음
            else:
                current = current.next  # 노드 이동
        return False


    def remove(self, target):
        """
        노드 삭제 함수
        :param target: 삭제할 노드 이름
        :return: None
        """
        if self.head.data == target:
            self.head = self.head.next
            print("이 문구는 첫번째 노드 삭제 시에만 볼 수 있어요")
            return
        current = self.head
        previous = None
        while current:
            if current.data == target:
                previous.next = current.next
            previous = current  # 현재 노드를 이전 노드로 지정
            current = current.next  # current가 다음 노드로 이동


    def __str__(self):  # 매직메서드로 print 함수등에 출력할 내용을 정리
        n = self.head
        while n is not None:
            print(n.data, end="   ")
            n = n.next  # 다음 노드로 이동
        return '[끝]'


pokemon_list = LinkedList()
pokemon_list.append('꼬부기')
pokemon_list.append('피카츄')
pokemon_list.append('뮤')
pokemon_list.append('파이리')
print(pokemon_list)
pokemon_list.append('라이츄')
print(pokemon_list)
# pokemon_list.remove('꼬부기')  # 첫 번째 노드 삭제
pokemon_list.remove('뮤')
print(pokemon_list)