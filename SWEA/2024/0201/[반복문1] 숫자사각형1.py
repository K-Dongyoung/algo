"""
사각형의 높이 H와 너비 W가 주어지면
H행 W열의 사각형 모양으로 1부터 H*W까지 숫자가 차례대로 출력 하시오.

숫자의 진행 순서는 처음에 맨 윗줄의 왼쪽에서 오른쪽으로 1부터 차례대로 너비 W 만큼 출력한 후
다음 줄로 바꾸어서 다시 왼쪽에서 오른쪽으로 1씩 증가하면서 출력하는 방법으로 H번 줄까지 반복한다.

<제한조건>
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 H와 W가 주어진다. ( 1 ≤ H, W ≤ 100 )

입력
3
1 1
2 3
4 5
"""
T = int(input())
for tc in range(1, T+1):
    H, W = list(map(int, input().split()))
    A = [[i] * W for i in range(H)]
    print(f'#{tc}')
    for i in range(H):
        for j in range(W):
            A[i][j] = i * W + j + 1
            print(A[i][j], end=' ')
        print()