import numpy as np  # Third party. 별도 설치 필요

# numpy 배열 생성
np_array = np.array([3, '2', 1.7])  # 이질적인 원소들
print(np_array, type(np_array))  # 한 가지 타입(상위 타입)으로 모두 변환됨. 속도에 장점

# python 리스트 생성
list_array = [3, '2', 1.7]  # 이질적인 원소들
print(list_array, type(list_array))  # 그대로 출력. 속도는 단점
