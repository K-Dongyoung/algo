def solution(n, stations, w):
    answer = 0
    a = 0  # 5g가 닿지 않는 아파트 범위 첫 아파트의 바로 전 아파트 번호 저장할 변수

    for apt in stations:  # 각 apt 기지국 앞쪽에 추가로 설치해야 할 기지국 수 계산하여 answer에 더함
        _4g = apt - w - 1 - a  # 기지국 설치된 apt 이전 범위에서 5g가 닿지 않는 아파트 수
        answer += _4g // (2 * w + 1)  # 설치해야 할 기지국 수 계산: (2 * w + 1)는 하나의 기지국이 커버하는 아파트 수
        if _4g % (2 * w + 1):  # (2 * w + 1)보다 작은 수의 아파트에 대해 추가로 하나 더 설치해야 함
            answer += 1
        a = apt + w

    _4g = n - a  # stations 마지막 아파트 이 후 n번 아파트 까지 기지국 계산
    answer += _4g // (2 * w + 1)
    if _4g % (2 * w + 1):
        answer += 1

    return answer
