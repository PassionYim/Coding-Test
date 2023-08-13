n, m = map(int, input().split())
i, j, dir = map(int, input().split())
datas = []
for _ in range(n):
    datas.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(datas)