n = int(input())
count = 0
while n != 0:
    if n & 1:
        count += 1
    n >>= 1
print(count)
