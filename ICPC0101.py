n = int(input())
arr = [int(x) for x in input().split()]
stack = []
for x in arr:
    if len(stack) > 0 and (x + stack[-1]) % 2 == 0:
        stack.pop()
    else: 
        stack.append(x)
print(len(stack))
