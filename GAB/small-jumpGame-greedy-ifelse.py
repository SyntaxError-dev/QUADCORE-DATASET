def minJumps(arr):
    n = len(arr)
    if arr[0] == 0:
        return -1
    maxReach = 0
    currReach = 0
    jump = 0
    for i in range(n):
        maxReach = max(maxReach, i + arr[i])

        if maxReach >= n - 1:
            return jump + 1

        # Increment the Jump as we reached the
        # Current Reachable index
        if i == currReach:

            # If Max reach is same as current index
            # then we can not jump further
            if i == maxReach:
                return -1

            # If Max reach > current index then increment
            # jump and update current reachable index
            else:
                jump += 1
                currReach = maxReach

    return -1


if __name__ == "__main__":
    arr = [1, 3, 2, 2, 1, 4, 6]
    print(minJumps(arr))
