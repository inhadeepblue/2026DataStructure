import random
from idlelib import search


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


    def __str__(self):  # 매직메서드로 print 함수등에 출력할 내용을 정리
        n = self.head
        while n is not None:
            print(n.data, end=" ")
            n = n.next  # 다음 노드로 이동
        return '[끝]'


lotto_number_list = LinkedList()
# 중복 값이 나올 수 있음 (주의)
for i in range(6):  # 0~5
    lotto_number = random.randint(1, 45)
    lotto_number_list.append(lotto_number)

print(lotto_number_list)  # __str__
print(lotto_number_list.search(33))

help(print)  # print 함수 매뉴얼
help(LinkedList.append)  # 연결리스트 클래스의 멤버함수 append 매뉴얼