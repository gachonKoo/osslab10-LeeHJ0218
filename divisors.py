# divisors.py
import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit(0)

try:
    n = int(data[0])
except:
    sys.exit(0)

if n == 0:
    print(0)
else:
    n = abs(n)
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
