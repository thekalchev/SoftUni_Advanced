n = int(input())
codes = set()
for _ in range(n):
    code = input()
    codes.add(code)

while True:
    code = input()
    if code == 'END':
        break
    if code in codes:
        codes.remove(code)

print(len(codes))
for code in sorted(codes):
    print(code)

