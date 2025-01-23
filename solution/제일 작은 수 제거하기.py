def solution(arr):
    answer = []
    if len(arr) == 1:           # arr 배열의 길이가 1과 같으면 answer에 -1을 추가
        answer.append(-1)
    else :
        answer = arr                
        answer.remove(min(arr)) # arr 배열 값들을 answer에 넣은 후 arr의 최솟값을 제거
    return answer               # answer 값을 리턴


print(solution([4,3,2,1]))
print(solution([10]))