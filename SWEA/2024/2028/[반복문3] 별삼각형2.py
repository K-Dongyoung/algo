"""
삼각형의 높이 N과 종류 M을 입력 받은 후 출력과 같은 삼각형 모양으로 별을 출력하는 프로그램을 작성하시오.

<입력조건>
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 크기 N과 종류 M이 주어진다.(1<= N <= 10, 1 <= M <= 4, N과 M은 홀수)
"""
# 리스트를 구조분해 할당으로 그냥 출력하는 거랑 join해서 문자열로 출력하는 거랑 문자 사이의 간격이 다름!
# 리스트를 구조분해 할당으로 그냥 출력하는 거랑 join해서 문자열로 출력하는 거랑 문자 사이의 간격이 다름!
# 리스트를 구조분해 할당으로 그냥 출력하는 거랑 join해서 문자열로 출력하는 거랑 문자 사이의 간격이 다름!
# 리스트를 구조분해 할당으로 그냥 출력하는 거랑 join해서 문자열로 출력하는 거랑 문자 사이의 간격이 다름!
# 리스트를 구조분해 할당으로 그냥 출력하는 거랑 join해서 문자열로 출력하는 거랑 문자 사이의 간격이 다름!
# 리스트를 구조분해 할당으로 그냥 출력하는 거랑 join해서 문자열로 출력하는 거랑 문자 사이의 간격이 다름!
# 리스트를 구조분해 할당으로 그냥 출력하는 거랑 join해서 문자열로 출력하는 거랑 문자 사이의 간격이 다름!
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    L = [[' '] * N for _ in range(N)]

    if M==1:
        for col in range(N//2+1):
            for row in range(col, N-col):
                L[row][col] = '*'

    elif M==2:
        for col in range(N//2+1):
            for row in range(N//2-col, N//2+col+1):
                L[row][col] = '*'

    elif M==3:
        for row in range(N):
            for col in range(row, N-row):
                L[row][col] = '*'
                L[N-row-1][col] = '*'

    elif M==4:
        for row in range(N//2+1):
            for col in range(row, N//2+1):
                L[row][col] = '*'
        for col in range(N//2, N):
            for row in range(col, N):
                L[row][col] = '*'

    print(f"#{tc}")
    for i in range(N):
        print(''.join(L[i]))

"""
입력
4
5 1
5 2
5 3
5 4

출력
#1
*
**
***
**
*
#2
  *
 **
***
 **
  *
#3
*****
 ***
  *
 ***
*****
#4
***
 **
  *
  **
  ***
"""