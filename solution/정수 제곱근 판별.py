def solution(n):
    x = n ** (1/2)  # n의 제곱근을 계산해서 x에 대입
    if x % 1 == 0:  # x를 1로 나누어서 나머지가 0이면 정수
        return (x+1)**2 # 정수이니까 x+1의 제곱근 반환환
    else:
        return -1 # 정수가 아니면 -1 반환환

print(solution(121))
print(solution(3))