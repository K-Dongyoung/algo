"""
백준에서는 테스트 케이스가 파일 형식으로 제공되는 것이 아니라,
문제를 제출하면 입력 데이터가 표준 입력(stdin)으로 제공됩니다.
이는 프로그램이 실행될 때 입력이 자동으로 주어지는 형태로,
직접 파일을 업로드하거나 읽을 필요가 없습니다.

파이참에서 작성한 코드와 백준에서 사용하는 표준 입력을 사용하는 코드 간의 속도 차이는
주로 입력 방식에서 발생합니다.
input() 함수는 한 번 호출할 때마다 시스템 호출을 수행하기 때문에,
많은 입력을 처리할 때 느려질 수 있습니다.
반면, sys.stdin.read를 사용하면 한 번에 모든 입력을 읽어 들여 이를 처리하기 때문에
훨씬 빠르게 동작합니다.
"""
import sys
input = sys.stdin.read

data = input().strip().split()
N = int(data[0])
x = []
y = []

for i in range(N):
    x.append(int(data[2 * i + 1]))
    y.append(int(data[2 * i + 2]))

print((max(x) - min(x)) * (max(y) - min(y)))

"""
다른 사람 코드
N, *point = map(int, open(0).read().split())
dist = lambda x:max(x)-min(x)
print(dist(point[::2])*dist(point[1::2]))
"""