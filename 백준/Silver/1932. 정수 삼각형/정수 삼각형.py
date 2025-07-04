def max_path(row, col):
    if row == _size -1:
        return _triangle[row][col]

    path_left = _triangle[row][col] + max_path(row+1, col)
    path_right = _triangle[row][col] + max_path(row+1, col+1)

    return max(path_left, path_right)


_triangle = []
_size = int(input())
for _ in range(_size):
    _triangle.append(list(map(int, input().split())))


for i in range(_size-1, 0, -1):
    for j in range(len(_triangle[i])-1):
        _triangle[i-1][j] += max(_triangle[i][j], _triangle[i][j+1])


print(_triangle[0][0])
