def solution(s):  
    arr = s.split(' ') # 공백을 기준으로 문자열을 나누어 배열에 저장
    for word in range(len(arr)): # 배열의 길이만큼 반복
        result = '' # 결과를 저장할 변수
        for i in range(len(arr[word])): # 배열의 문자열 길이만큼 반복
            if i % 2 == 0:  # 짝수번 째 문자열이면 대문자로 변환해서 저장
                result += arr[word][i].upper() 
            else:           # 아닌경우 소문자로 변환해서 저장
                result += arr[word][i].lower()
        arr[word] = result  # 배열에 저장
    return ' '.join(arr)    # 배열을 공백 기준으로 문자열 변환해서 출력

print(solution("try hello world")) 