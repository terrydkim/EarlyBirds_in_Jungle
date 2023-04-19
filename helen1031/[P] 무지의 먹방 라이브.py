def solution(food_times, k):
    if sum(food_times) < k:
        return -1

    current = 0
    time = 0
    while time < k:
        if food_times[current] != 0:
            food_times[current] -= 1
            current = (current + 1) % len(food_times)
        else:
            current = (current + 1) % len(food_times)
            continue

        time += 1

    return current + 1