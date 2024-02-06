def transpose_arr(arr, R, C):
    arr_transposesd =[]
    for i in range(C):
        row_result = []
        for j in range(R):
            row_result.append(arr[j][i])
        arr_transposesd.append(row_result)
    return arr_transposesd


R, C = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(R)]
print(transpose_arr(arr, R, C))
