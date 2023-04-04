

def solution(today, terms, privacies):
    # 오늘날짜, 1차원 배열 유효기간, 1차원 배열 정보
    # today "2022.05.19"
    # Terms ["A 6", "B 12", "C 3"]
    # privacies ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    # 파기 번호 오름차순 1차원 배열에 담고 리턴
    answer = []
    today = today.split('.')
    terms_lst = []
    for i in range(len(terms)):
        a,b = terms[i].split()
        terms_lst.append((a,b))
    privacies_lst = []
    for i in range(len(privacies)):
        a,b= privacies[i].split()
        c,d,e = privacies[i].split('.')
        privacies_lst.append((a,c,d,e,b))
    # privacies[0].split()
    print(privacies[0].split())



    return answer
# dic 써야함?
# find로 term[0]을 찾고 term[1]가지고 계산
today = "2022.05.19"
today = today.split('.')
print(today)
# privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
# a,b = privacies[0].split()
# c,d,e = privacies[0].split('.')
# print(c,d,e)

