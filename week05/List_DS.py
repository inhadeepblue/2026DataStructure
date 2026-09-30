# C++ 배열 (동질적 원소를 갖는다)
# #include <iostream>
# using namespace std;
#
# int main() {
# 	int a[5] = {3, -9, 77, 8, 10};  // 모두 정수
# 	int a[5] = {3, -9, 77.9, 8, 10};  // 77.9 실수로. 컴파일 에러
# 	cout << a[1] << '\n';
# }

# artists = []
artists = list()
print(artists)
artists.append("리센느")
print(artists)
artists.append("핑클")
artists.append("데이식스")
print(artists)
print(artists.pop(1))  # 1번 인덱스 위치의 값을 리턴하고 삭제
print(artists)
print(artists[1])
artists.append(77.9)   # 파이썬의 리스트는 실수(실수 뿐만 아닌 다른 타입들 모두 포함)도 앞서 삽입한 문자열들과 같이 담을 수 있다
print(artists)