def solution(s):
    if len(s) % 2 == 1:    # 홀수인지 확인
        return s[len(s)//2] # 홀수이면 s 길이를 2로 나눠 나오는 가운데 수 출력
    else:
         return s[len(s) // 2 - 1:len(s) // 2 + 1] # 짝수인 경우 s길이를 2로 나눠 -1과 +1을 해줘 중앙 인덱스의 앞뒤 문자 출력
    
print(solution("abcde"))