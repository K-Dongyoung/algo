def enQ(data):
    global rear
    if rear == Qsize - 1: # 가득 차면
        print('Q is Full')
    else:
        rear += 1
        Q[rear] = data

def deQ():
    global front
    if front == rear:
        print('empty')
        return -1
    else:
        front += 1
        return Q[front]



Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1
enQ(1)
enQ(2)
rear += 1
Q[rear] = 3     # enqueue(3)
enQ(4)

while front != rear:
    front += 1
    print(Q[front])

# print(deQ())
# print(deQ())
# front += 1
# tmp = Q[front]
# print(tmp)
