N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
works = sorted(works, key=lambda x: x[1])
total_time = 0
min_rest = float("inf")
for time, limit in works:
    total_time += time
    min_rest = min(min_rest, limit - total_time)
    # 총시간이 더 커지는경우는 제외하기 위해서 넣었다.
    if limit < total_time:
        print(-1)
        exit()
print(min_rest)