str = input()  # 사용자로부터 문자열을 입력받음

for i in str:   # 입력된 문자열의 각 문자에 대해 반복   

    if i.isupper() == True:     # 대문자일 경우 소문자로 변환하여 출력합니다.    
        print(i.lower(), end="")  
    else:                       # 소문자일 경우 대문자로 변환하여 출력합니다.  
        print(i.upper(), end="")  
