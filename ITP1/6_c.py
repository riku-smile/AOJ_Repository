n = int(input())
building = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]

for i in range(n):
    b, f, r, v = map(int, input().split())
    building[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print(f' {building[i][j][k]}', end="")
        print()
    if int(i) < 3:
        print('#'*20)
