str, n = input().strip().split(' ') # 공백을 기준으로 나눈다(strip를 이용하여 앞 뒤 공백 제거)
n = int(n) # 두 번째 입력값 n 정수로 반환

if n>=1: 
    print(str * n) # n이 1보다 크거나 같으면 str을 n번만큼 곱해서 출력
else:
    print(" ") # 아닌 경우 공백 출력