def solution(num):  
    if num % 2 == 0: # 짝수일 경우
        return "Even" # Even 출력
    else:         # 홀수일 경우
        return "Odd"    # Odd 출력
    
print(solution(3))
print(solution(4))