class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index

    def get_data(self):
        return self.data

    def get_index(self):
        return self.index


def merge(arr):
    if len(arr) == 1:
        return
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    merge(left)
    merge(right)
    index_left = index_right = index = 0
    result = [None] * (len(left) + len(right))
    while index_left < len(left) and index_right < len(right):
        if left[index_left].data <= right[index_right].data:
            result[index] = Node(left[index_left].data, left[index_left].index)
            print(left[index_left].index, end=' ')
            index_left += 1
        else:
            result[index] = Node(right[index_right].data, right[index_right].index)
            print(right[index_right].index, end=' ')
            index_right += 1
        index += 1
    while index_left < len(left):
        result[index] = Node(left[index_left].data, left[index_left].index)
        print(left[index_left].index, end=' ')
        index_left += 1
        index += 1
    while index_right < len(right):
        result[index] = Node(right[index_right].data, right[index_right].index)
        print(right[index_right].index, end=' ')
        index_right += 1
        index += 1
    for i in range(len(arr)):
        arr[i] = result[i]
    print()
    return arr


n = int(input())

sum_matrix = []

for i in range(n):
    amount_matrix = int(input())
    sum = 0
    for y in range(amount_matrix):
        elements = list(map(int, input().split()))
        sum += elements[y]
    sum_matrix.append(Node(sum, i))
merge(sum_matrix)
for i in range(n):
    print(sum_matrix[i].index, end=' ')
