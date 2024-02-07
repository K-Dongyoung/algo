"""
삼각형의 높이 N과 종류 M을 입력 받은 후 출력 같은 삼각형 형태로 출력하는 프로그램을 작성하시오.

(1)
*
**
***

(2)
***
**
*

(3)
  *
 ***
*****

<입력조건>
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 크기 N과 종류 M이 주어진다.(1<= N <= 10, 1 <= M <= 3)
"""
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    print(f"#{tc}")

    if M==1:
        for i in range(N):
            for j in range(i+1):
                print("*", end="")
            print()

    elif M==2:
        for i in range(N):
            for j in range(N-i):
                print("*", end="")
            print()

    else:
        for i in range(N):
            print(" "*(N-i-1), end="")
            print("*"*(2*i+1))


"""
입력
3
3 1
3 2
3 3

출력
#1
*
**
***
#2
***
**
*
#3
  *
 ***
*****
"""