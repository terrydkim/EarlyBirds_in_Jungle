# 백준 14501 퇴사
# Fail

today = "2022.05.19"	
terms = ["A 6", "B 12", "C 3"]	
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


Y = today[2:4]
M = today[5:7]
D = today[8:10]

terms_dict = dict()
for t in terms:
    
    alpha = t[0]
    month = t[-1]
    terms_dict[alpha] = int(month)

result = []
for p in privacies:
    
    p_Y = p[2:4]
    p_M = p[5:7]
    p_D = p[8:10]
    p_alpha = p[-2]
    
    plus_month = terms_dict.get(p_alpha)


    new_month = plus_month + p_M
    if new_month > 12:
        p_Y += 1
        new_month -= 12
    
    #
    if Y < p_Y:
        result.append(privacies.index(p)+1)
        continue
    
    if M < new_month:
      result.append(privacies.index(p)+1)
      continue

    if D < p_D-1:
      result.append(privacies.index(p)+1)
      continue

print(result)
        
    
        





    
    
    
