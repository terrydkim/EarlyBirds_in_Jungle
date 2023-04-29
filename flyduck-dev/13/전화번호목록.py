def solution(phone_book):
    answer = True
    dict = {}
    for i in range(len(phone_book)):
        dict[phone_book[i]] = i
    for key in dict:
        target = ""
        for j in key:
            target = target + j
            if target == key:
                break
            check = dict.get(target, -1)
            if check > -1:
                answer = False
                break

    return answer