t = int(input())

for i in range(t):
    a = int(input())
    b = input().split()
    result = 0
    for i in b:
        result += int(i)
    print(result)