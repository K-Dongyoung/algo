for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    max_i = 0
    min_i = 0

    for i in range(dump):
        for j in range(len(box)):
            if box[max_i] < box[j]:
                max_i = j
            if box[min_i] > box[j]:
                min_i = j
        box[max_i] -= 1
        box[min_i] += 1

    for j in range(len(box)):
        if box[max_i] < box[j]:
            max_i = j
        if box[min_i] > box[j]:
            min_i = j


    print(f'#{tc} {box[max_i] - box[min_i]}')


