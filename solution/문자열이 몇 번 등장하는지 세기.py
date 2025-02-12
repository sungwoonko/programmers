def solution(myString, pat):  
    count = 0  
    pat_length = len(pat)   # pat의 길이를 pat_length로 받는다
    myString_length = len(myString)   # myString의 길이를 myString_length로 받는다

    for i in range(myString_length - pat_length + 1):     
        if myString[i:i + pat_length] == pat:  # 현재 위치 i에서 pat의 길이만큼의 부분 문자열을 잘라서 pat과 비교
            count += 1  # 위에 조건이 맞으면 count를 1 올린다
            
    return count