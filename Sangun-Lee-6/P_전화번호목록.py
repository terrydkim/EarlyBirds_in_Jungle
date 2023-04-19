def solution(phone_book):
    
    # 1. hash_map 만들기
    hash_map = {}
    for phone_num in phone_book:
        hash_map[phone_num] = 1         # 1은 존재함을 의미
        
    
    # 2. 접두어가 hash map 에 존재하는지 확인
    for phone_num in phone_book:
        prefix = ""
        for num in phone_num:
            prefix += num
            
            # 3. hash_map 에서 접두어 찾기
            if prefix in hash_map and prefix != phone_num:
                return False
            
    
    return True