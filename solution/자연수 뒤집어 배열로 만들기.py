def solution(n):
    return list(map(int, reversed(str(n)))) # 입력받은 정수 n을 문자열로 바꾼다음 reversed로 뒤집고 그리고 다시 map으로 정수로 바꾼 후 리스트형태로 출력

print(solution(12345))