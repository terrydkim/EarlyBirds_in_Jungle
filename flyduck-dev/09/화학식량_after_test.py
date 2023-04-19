import sys
input = sys.stdin.readline
stack = []
ch_str = input().rstrip()

answer = 0
dic = {"H":1, "C":12, "O":16}
for char in ch_str:
    if char in "23456789":
        target = stack.pop()
        stack.append(target*int(char))
    if char in "CHO":
        stack.append(dic[char])
    if char in "(":
        stack.append(char)
    if char in ")":
        temp = 0
        while stack[-1] != "(":
            temp += stack.pop()
        stack.pop()
        stack.append(temp) 

print(sum(stack))

