n = int(input().strip())
if n == 0:
    print(0)
else:
    n = abs(n)
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
