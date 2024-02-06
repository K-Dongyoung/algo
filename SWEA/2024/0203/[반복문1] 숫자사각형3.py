"""
사각형의 높이 H와 너비 W를 입력받은 후
H행 W열의 사각형 형태로 1부터 H*W번까지 숫자가 차례대로 출력하시오.

숫자의 진행 순서는 처음에 왼쪽에서 오른쪽으로 너비 W만큼 진행 한 후 방향을 바꾸어서 이를 반복한다.

<제한조건>
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 10 )
각 케이스의 첫 줄에 H와 W가 주어진다. ( 1 ≤ H, W ≤ 10 )

3
1 1
2 3
4 5

#1
1
#2
1 2 3
6 5 4
#3
1 2 3 4 5
10 9 8 7 6
11 12 13 14 15
20 19 18 17 16
"""

T = int(input())
for tc in range(1, T+1):
    H, W = list(map(int, input().split()))
    print(f"#{tc}")
    for i in range(H):
        for j in range(W):
            # print(i*W + j + 1, end=" ")
            # print((i+1)*W - j, end=" ")
            print((i + i % 2) * W + j + 1 - (i % 2) * j * 2 - (i % 2), end=" ")
        print()