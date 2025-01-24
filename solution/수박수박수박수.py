def solution(n):
    p = "수박"      # P라고 수박이라는 패턴을 만들어준다.   
    return (p * (n//2)) + p[:n%2]   # N이 2로 나눈 몫을 P에 곱해주고 그리고 N을 2로 나눴을 때 나머지 값을 인데싱을 해줘 그 해당되는 인덱싱 값만 가져온다.(짝수면 앞에만 실행되고 홀수면 뒤에까지 같이 실행된다.)

print(solution(1))
print(solution(3))
print(solution(4))