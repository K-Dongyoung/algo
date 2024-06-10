def solution(n, t, m, timetable):
    # 1. 각 버스에 타는 사람 찾기
    timetable.sort()  # HH:MM 형식 정렬이 되네, 대소 비교도 되네
    riders = [[] for _ in range(n)]  # 각 시간 별 버스에 탈 사람 저장할 리스트
    j = 0  # timetable while 순회할 때 사용할 인덱스
    num_ppl = len(timetable)
    for i in range(n):
        seat = m
        bustime = 9 * 60 + i * t
        riders[i].append(bustime)
        while j < num_ppl:
            time = int(timetable[j][:2]) * 60 + int(timetable[j][3:5])
            if seat > 0 and time <= bustime:
                riders[i].append(time)
                seat -= 1
                j += 1
            else:
                break

    # 3. 마지막 버스가 자리가 남는지 꽉 차는지 구분
    # 자리 남으면 버스 도착 시간에 도착하면 됨
    if len(riders[n - 1]) < m + 1:
        hour = riders[n - 1][0] // 60
        minute = riders[n - 1][0] % 60
        answer = f"{hour:02d}:{minute:02d}"

    # 자리 부족하면 마지막에 타는 사람보다 1분 일찍 도착하면 됨
    else:
        time = riders[n - 1][m] - 1
        hour = time // 60
        minute = time % 60
        answer = f"{hour:02d}:{minute:02d}"

    return answer


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
