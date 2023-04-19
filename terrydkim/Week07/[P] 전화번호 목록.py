def solution(phone_book):
    answer = True
    phone = sorted(phone_book)

    # print(phone[1][:len(phone[0])])
    for i in range(len(phone)-1):
        if phone[i] == phone[i+1][:len(phone[i])]:
            answer = False
            return answer
    
    return answer
