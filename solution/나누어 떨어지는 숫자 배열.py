def solution(arr, divisor):  
    answer = []    
    for num in arr:             # arr의 배열 수 만큼 반복    
        if num % divisor == 0:  # num이 divisor로 나눴을 때 나머지가 0이면
            answer.append(num)  # anwser 배열 안에 num값 대입

    if not answer:              # answer 값이 비어있으면 -1 반환 
        return [-1]  
    else:                       # 아니면 오름차순으로 정렬해서 반환
        return sorted(answer)
    
print(solution([5,9,7,10],5))
print(solution([2,36,1,3],1))
print(solution([3,2,6],10))