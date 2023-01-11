input = __import__('sys').stdin.readline
import sys
n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append((b,a))
l.sort(reverse=True)
last = l[0][0]
for i in l:
    last = min(last,i[0])-i[1]
    if last<0: print(-1); sys.exit()
print(last)