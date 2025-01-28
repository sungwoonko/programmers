def solution(n, m):
    # 최대 공약수 구하기
    for i in range(min(n, m), 0, -1):   # n, m 중 작은 수를 골라 1까지 거꾸로 반복
        if (n % i == 0) and (m % i == 0): # n, m이 i로 나누었을 때 나머지가 둘 다 0이 되는 수 찾기
            a = i   # 찾은 i 값을 a에 대입
            break
    # 최소 공배수 구하기        
    for j in range(max(n, m), (n * m) + 1): # n, m 중 큰 수를 골라 nm까지 반복
        if j % n == 0 and j % m == 0: # j에 대해 n,m이 나누어 떨어지는 수 구하기
            b = j   # j 값을 b에 대입
            break
        
    return [a, b]   # a,b를 리턴     

print(solution(3,12))
print(solution(2,5))