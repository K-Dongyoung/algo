while True:
    n = int(input())

    if n == -1:
        break

    answer = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            answer.append(f"{i}")
            sum += i
    if sum == n:
        print(f"{n} = {' + '.join(answer)}")  # print(f"{n} =" + " + ".join(answer))
    else:
        print(f"{n} is NOT perfect.")
