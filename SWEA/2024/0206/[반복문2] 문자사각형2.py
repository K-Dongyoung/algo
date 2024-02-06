"""
정사각형의 한 변의 길이 n을 입력받은 후 다음과 같은 문자로 된 정사각형 형태로 출력하는 프로그램을 작성하시오.

문자의 진행 순서는 왼쪽 위에서부터 아래쪽으로 ‘A'부터 차례대로 채워나가고
다시 오른쪽 아래부터 위쪽으로 채워나가는 방법으로 아래 표와 같이 채워 넣는다.
'Z' 다음에는 다시 'A'부터 반복된다.

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
A F G
B E H
C D I
#3
A J K T U
B I L S V
C H M R W
D G N Q X
E F O P Y

V Q L G B
U P K F A
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    count = 0

    L = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            L[j + (i % 2) * (N - 2 * j - 1)][i] = chr(65 + count)
            count += 1
            count %= 26

    print(f"#{tc}")
    for i in range(N):
        print(*L[i])