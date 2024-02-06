"""
삼각형의 높이 N을 입력받아서 출력과 같이 문자 'A'부터 차례대로 왼쪽 대각선으로 채워서
삼각형 모양을 출력하는 프로그램을 작성하시오.

오른쪽 위부터 왼쪽 아래쪽으로 이동하면서 문자 'A'부터 차례대로 채워나간다.
 N번 행까지 채워지면 다시 오른쪽 둘째 행부터 왼쪽 아래로 채워나간다.
삼각형이 모두 채워질 때까지 반복하면서 채워 나간다. (문자 'Z'다음에는 'A'부터 다시 시작한다.)

< 처리조건 >
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 N이 주어진다. ( 1 ≤ N ≤ 10 )

<힌트>
ASCII 코드를 문자로 바꾸는 함수는 chr()이고
문자를 ASCII코드로 바꾸는 함수는 ord()이다.
(예) ord('A') , chr(65)

3
1
3
5

#1
A
#2
  A
 B D
C E F
#3
    A
   B F
  C G J
 D H K M
E I L N O
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    L = [[''] * (2 * N - 1) for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(i, N):
            L[j][N - 1 - j + i] = chr(65 + count)
            count += 1
            count %= 26

    print(f"#{tc}")
    for i in range(N):
        print(*L[i])