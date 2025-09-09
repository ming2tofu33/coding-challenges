import sys

input = sys.stdin.readline

m = int(input())
s = set()
out = []

for _ in range(m):
    line = input().strip()
    if line == "all":
        s = set(range(1, 21))
    elif line == "empty":
        s.clear()
    else:
        op, xs = line.split()
        x = int(xs)
        if op == "add":
            s.add(x)
        elif op == "remove":
            s.discard(x)
        elif op == "check":
            out.append('1' if x in s else '0')
        elif op == "toggle":
            if x in s:
                s.remove(x)
            else:
                s.add(x)

sys.stdout.write("\n".join(out))