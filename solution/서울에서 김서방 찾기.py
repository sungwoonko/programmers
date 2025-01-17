def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            answer = i
            break
            
    return '김서방은 ' + str(answer) + '에 있다'    
    
print (solution(["Jane", "Kim"]))