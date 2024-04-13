import numpy as np
print("첫 번째 프로젝트 테스트입니다.")
a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9],
              [0,1,2]])
print(a[:,-1:])
print("\n")
print(a[:,2:3])
print("\n")
print(a[1:3,1:2])