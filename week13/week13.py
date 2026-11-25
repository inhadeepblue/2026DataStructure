# 파이썬 내장 자료구조 리스트를 이용한 스택처럼 사용
tasks = list()
print(tasks)
tasks.append('자료구조')
tasks.append('점심')
tasks.append('예배')
print(tasks)
print(tasks.pop())
print(tasks)
#print(tasks.peek())  # 파이썬의 리스트에는 peek함수가 존재하지 않음. Error
print(tasks[-1])  # 기존에 Stack 클래스 설계 했을 때의 peek 기능. (역방향 인덱싱)
print(len(tasks)-1)
print(tasks[len(tasks)-1])  # 정방향 인덱싱
print(tasks)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class Stack:
#     def __init__(self):
#         self.top = None
#
#     def push(self, data):
#         node = Node(data)
#         if self.top is None:
#             self.top = node
#         else:
#             node.next = self.top
#             self.top = node
#
#     def pop(self):
#         if self.top is None:
#             raise IndexError('스택이 비어 있습니다. 삭제 불가!')
#         popped_node = self.top
#         self.top = self.top.next
#         return popped_node.data
#
#
# subjects = Stack()
# subjects.push("자료구조")
# subjects.push("웹프로그래밍")
#
# for i in range(2):
#     print(subjects.pop())
#
# numbers = Stack()
# numbers.push(3.14)
# numbers.push(2.71)
# numbers.push(55.5)
#
# for i in range(4):  # i가 3일때 즉 4번째 턴에 예외 발생
#     print(numbers.pop())
