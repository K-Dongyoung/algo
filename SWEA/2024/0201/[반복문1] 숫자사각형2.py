"""
사각형의 높이 H과 너비 W가 주어지면
H행 W열의 사각형 모양으로 1부터 H*W까지 숫자가 차례대로 출력 하시오.

숫자의 진행 순서는 처음에 왼쪽 위에서 아래쪽으로 H만큼 진행 한 후
바로 오른쪽 위에서 다시 아래쪽으로 진행하는 방법으로 사각형이 될 때까지 반복한다.

<제한조건>
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 H와 W가 주어진다. ( 1 ≤ H, W ≤ 10 )

입력
3
1 1
2 3
4 5

출력
#1
1
#2
1 3 5
2 4 6
#3
1 5 9 13 17
2 6 10 14 18
3 7 11 15 19
4 8 12 16 20
"""

T = int(input())
for tc in range(1, T+1):
    H, W = list(map(int, input().split()))
    print(f'#{tc}')
    for i in range(H):
        for j in range(W):
            print(i+1+j*H, end=' ')
        print()