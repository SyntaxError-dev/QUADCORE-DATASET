s = "leEeetcode"

stack = []

for i in range(len(s)):
    char = s[i]

    if len(stack) > 0:
        last_char = stack[len(stack) - 1]

        if abs(ord(char) - ord(last_char)) == 32:
            stack.pop()
        else:
            stack.append(char)
    else:
        stack.append(char)

result = ""
for c in stack:
    result = result + c

print(result)