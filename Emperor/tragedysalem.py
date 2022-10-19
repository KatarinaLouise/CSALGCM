n, f, k = list(map(int, input().rstrip().split(" ")))
vamps = [int(input()) for x in range(n)]
ans = "NO"
vamps.sort()  # sort the array first
total = sum(vamps[:k])  # get k vampires -> vampires daddy has to stab <3
if total <= f:
    ans = "YES"

print(ans)
