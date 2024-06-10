# 테스트 케이스 세 개 틀림.. 왜??
def solution(n, t, m, timetable):
    # 1. 각 버스에 타는 사람 찾기
    timetable.sort()  # HH:MM 형식 정렬이 되네, 대소 비교도 되네
    riders = [[] for _ in range(n)]  # 각 시간 별 버스에 탈 사람 저장할 리스트
    j = 0  # timetable while 순회할 때 사용할 인덱스
    num_ppl = len(timetable)
    for i in range(n):
        seat = m
        bus_hour = 9 + ((n - 1) * t) // 60
        bus_min = (i * t) % 60

        bus_hour_s = f"{bus_hour}"
        if bus_hour < 10:
            bus_hour_s = f"0{bus_hour}"

        bus_min_s = f"{bus_min}"
        if bus_min < 10:
            bus_min_s = f"0{bus_min}"

        bustime_s = bus_hour_s + ":" + bus_min_s

        while j < num_ppl:
            if seat > 0 and timetable[j] <= bustime_s:
                riders[i].append(timetable[j])
                seat -= 1
                j += 1
            else:
                break

    # 3. 마지막 버스가 자리가 남는지 꽉 차는지 구분
    # 자리 남으면 버스 도착 시간에 도착하면 됨
    if len(riders[n - 1]) < m:
        if n == 1:
            answer = "09:00"
        else:
            last_bus_hour = 9 + ((n - 1) * t) // 60
            last_bus_minute = ((n - 1) * t) % 60

            last_bus_hour_s = f"{last_bus_hour}"
            if last_bus_hour < 10:
                last_bus_hour_s = f"0{last_bus_hour}"

            last_bus_minute_s = f"{last_bus_minute}"
            if last_bus_minute < 10:
                last_bus_minute_s = f"0{last_bus_minute}"

            answer = last_bus_hour_s + ":" + last_bus_minute_s

    # 자리 부족하면 마지막에 타는 사람보다 1분 일찍 도착하면 됨
    else:
        last_person = riders[n - 1][m - 1]

        hour = int(last_person[:2])
        minute = int(last_person[3]) * 10 + int(last_person[4])

        if minute == 0:
            hour -= 1
            minute = 59
        else:
            minute -= 1

        if hour < 10:
            hour_s = f"0{hour}"
        else:
            hour_s = f"{hour}"

        if minute < 10:
            minute_s = f"0{minute}"
        else:
            minute_s = f"{minute}"

        answer = hour_s + ":" + minute_s

    return answer


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
