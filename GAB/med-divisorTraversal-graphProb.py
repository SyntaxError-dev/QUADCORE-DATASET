nums = [2, 3, 6]

prime2index = {}
index2prime = {}

# Build prime mappings
for i in range(len(nums)):
    num = nums[i]
    temp = num

    j = 2
    while j * j <= temp:
        if temp % j == 0:
            if j not in prime2index:
                prime2index[j] = []
            prime2index[j].append(i)

            if i not in index2prime:
                index2prime[i] = []
            index2prime[i].append(j)

            while temp % j == 0:
                temp = temp // j
        j += 1

    if temp > 1:
        if temp not in prime2index:
            prime2index[temp] = []
        prime2index[temp].append(i)

        if i not in index2prime:
            index2prime[i] = []
        index2prime[i].append(temp)

# Visited trackers
visitedIndex = []
for _ in range(len(nums)):
    visitedIndex.append(False)

visitedPrime = {}

# Manual DFS using a stack (beginner-friendly)
stack = [0]

while len(stack) > 0:
    index = stack.pop()

    if visitedIndex[index]:
        continue

    visitedIndex[index] = True

    if index in index2prime:
        for prime in index2prime[index]:
            if prime in visitedPrime and visitedPrime[prime]:
                continue

            visitedPrime[prime] = True

            for next_index in prime2index[prime]:
                if not visitedIndex[next_index]:
                    stack.append(next_index)

# Final check
canTraverse = True
for v in visitedIndex:
    if not v:
        canTraverse = False
        break

print(canTraverse)