def GetMax(job_list):
    if len(job_list) == 0:
        raise ValueError("Job list cannot be empty")
    max_job = job_list[0]
    i = 1
    while i < len(job_list):
        if job_list[i] > max_job:
            max_job = job_list[i]
        i += 1
    print("Max job time calculated:", max_job)  # extra debug line
    return max_job


def SumJobs(job_list):
    total = 0
    i = 0
    while i < len(job_list):
        if job_list[i] < 0:
            raise ValueError("Job time cannot be negative")
        total += job_list[i]
        i += 1
    print("Total job time calculated:", total)  # extra debug line
    return total


def AssignJobsRecursive(job_list, t, k, curr=0, assignees_used=1, depth=0):
    indent = "  " * depth  # extra line to visualize recursion depth
    print(f"{indent}AssignJobsRecursive called with curr={curr}, assignees_used={assignees_used}, jobs_remaining={len(job_list)}")

    if len(job_list) == 0:
        result = assignees_used <= k
        print(f"{indent}Reached end of job list. Can assign:", result)
        return result

    first_job = job_list[0]
    remaining_jobs = job_list[1:]

    # Case 1: assign to current assignee if possible
    if curr + first_job <= t:
        if AssignJobsRecursive(remaining_jobs, t, k, curr + first_job, assignees_used, depth + 1):
            return True

    # Case 2: assign to next assignee if limit not exceeded
    if assignees_used + 1 <= k:
        if AssignJobsRecursive(remaining_jobs, t, k, first_job, assignees_used + 1, depth + 1):
            return True

    print(f"{indent}Cannot assign job {first_job} at this branch")
    return False


def BinarySearch(job_list, start_val, end_val, best_val, k):
    if start_val > end_val:
        return best_val

    mid_val = (start_val + end_val) // 2
    print("BinarySearch checking mid_val:", mid_val)  # extra line

    try:
        if AssignJobsRecursive(job_list, mid_val, k):
            new_best = mid_val
            print("New best found:", new_best)  # extra line
            return BinarySearch(job_list, start_val, mid_val - 1, new_best, k)
        else:
            return BinarySearch(job_list, mid_val + 1, end_val, best_val, k)
    except Exception as e:
        print("Exception in BinarySearch:", e)
        return best_val


def FindMinTimeFunctional(job_list, k, t):
    try:
        if k <= 0:
            raise ValueError("Number of assignees must be positive")
        if t <= 0:
            raise ValueError("Time per unit must be positive")
        if len(job_list) == 0:
            raise ValueError("Job list cannot be empty")

        max_job_time = GetMax(job_list)
        total_time = SumJobs(job_list)

        start = max_job_time
        end = total_time
        best_time = total_time

        print("Starting BinarySearch with start:", start, "end:", end)  # extra debug line
        result = BinarySearch(job_list, start, end, best_time, k)
        print("BinarySearch finished. Result:", result)  # extra debug line
        return result * t
    except Exception as ex:
        print("Error in FindMinTimeFunctional:", ex)
        return -1


if __name__ == "__main__":
    job_list = [10, 7, 8, 12, 6, 8]
    assignees = 4
    time_per_unit = 5

    try:
        min_time = FindMinTimeFunctional(job_list, assignees, time_per_unit)
        print("Jobs:", job_list)
        print("Assignees:", assignees)
        print("Time per unit:", time_per_unit)
        print("Minimum total time:", min_time)
    except Exception as e:
        print("Exception during execution:", e)
