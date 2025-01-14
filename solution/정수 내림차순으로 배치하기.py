def solution(n):
    answer = list(str(n)) # 입력받은 정수 n을 문자열로 바꾼 후 list 형태로 바꾼다 why? sort를 사용하기 위해서
    answer.sort(reverse=True) # reverse = True 값을 넣어 내림차순으로 정렬
    return int("".join(answer)) # join으로 하나의 문자열로 결합 후 int 형태로 변환해서 출력

print (solution(118372))