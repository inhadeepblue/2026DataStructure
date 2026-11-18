# python list

# empty list
# subjects = []
# subjects = list()

subjects = ['자료구조']  # 초기값을 가진 리스트
subjects.append('웹프로그래밍')  # 추가
print(subjects)
# subjects.pop()  # 마지막 원소 삭제 (pop은 삭제전에 삭제할 값을 리턴하는 기능이 있음)
# print(subjects.pop())
subjects.pop(0)  # pop함수는 기본적으로 맨 마지막 원소를 리턴/삭제 하지만 pop함수의 인수값으로 인덱스 번호를 지정할 수 있다
print(subjects)
# 이 외에도 파이썬 리스트에는 remove, insert 등등의 함수가 있다