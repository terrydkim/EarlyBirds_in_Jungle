def solution(name):
    gap = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]

    answer = 0
    idx = 0
    while True:
        answer += gap[idx]
        gap[idx] = 0
        print(answer)

        # 모두 변경 완료
        if sum(gap) == 0:
            break

        # 이동 방향
        left = 1
        right = 1

        while gap[idx - left] == 0:
            left += 1
        while gap[idx + right] == 0:
            right += 1

        answer += min(left, right)
        idx = idx - left if left < right else idx + right
        print(answer, left, right, idx)

    return answer