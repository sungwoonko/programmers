def solution(x, n):
    answer = []
    
    for i in range(1, n + 1):
        answer.append(x * i)
        
    return answer

# 입력값
x = 2
n = 5

# 출력값
print(f"입력값: x={x}, n={n}")
print("출력값:", solution(x, n))
