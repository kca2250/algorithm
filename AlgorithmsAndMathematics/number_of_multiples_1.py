n, x, y = map(int, input().split())

# まずcountを定義
count = 0

# n回ループさせて余りが0になればcountに+1する
for i in range(n):
    if(i+1)%x == 0 or (i+1)%y == 0:
        count+=1

print(count)