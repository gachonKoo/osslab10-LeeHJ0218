# divisors.py
import sys

def read_number():
    # 1) 명령행 인자 우선
    if len(sys.argv) >= 2:
        try:
            return int(sys.argv[1])
        except:
            pass
    # 2) 아니면 표준입력으로
    data = sys.stdin.read().strip().split()
    if not data:
        return None
    try:
        return int(data[0])
    except:
        return None

n = read_number()
if n is None:
    # 입력이 없으면 아무 출력도 하지 않음 (자동채점 대비)
    sys.exit(0)

if n == 0:
    print(0)
else:
    n = abs(n)
    divisors = [str(i) for i in range(1, n + 1) if n % i == 0]
    # 한 줄에 공백으로 구분하여 출력(맨 끝에 줄바꿈)
    print(" ".join(divisors))
