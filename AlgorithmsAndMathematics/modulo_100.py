n = int(input())
arr_a = list(map(int, input().split()))

ans = sum(arr_a) % 100

print(ans)