"""
삼각형의 높이 N을 입력받아서 아래와 같이 문자 'A'부터 차례대로 맨 오른쪽 가운데 행부터 차례대로
아래와 같이 채워서 삼각형 모양을 출력하는 프로그램을 작성하시오.

오른쪽 가운데 행에 문자 'A'를 채우고 왼쪽 열로 이동하여 위에서 아래로 채워나간다.
가장 왼쪽 행까지 반복하여 모두 채워 나간다. (문자 'Z'다음에는 'A'부터 다시 시작한다.)

< 처리조건 >
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 N이 주어진다. ( 1 ≤ N ≤ 19 ), N은 홀수이다.

"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    L = [[""] * (N//2 + 1) for _ in range(N)]
    count = 0

    for i in range(N//2 + 1):
        for j in range(2*i + 1):
            L[N//2  - i + j][N//2 - i] = chr(65 + count)
            count += 1
            count %= 26

    print(f"#{tc}")
    for i in range(len(L)):
        print(*L[i])



"""
입력
3
1
3
5

출력
#1
A
#2
B
C A
D
#3
E
F B
G C A
H D
I
"""