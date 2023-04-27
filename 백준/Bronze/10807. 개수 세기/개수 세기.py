T = int(input())
N_list = list(map(int, input().split()))
k = int(input())

dictionary = {i : N_list[i] for i in range(len(N_list))}

cnt = 0
for key, value in dictionary.items():
    if value == k:
        cnt+= 1
print(cnt)