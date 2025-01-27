def solution(phone_number):
    length = len(phone_number)  # phone_number의 문자열 길이를 구해 length에 대입
    change_part = '*' * (length - 4) # length에서 - 4 값을 *를 곱해 change_part에 대입 
    last_four = phone_number[-4:]   # last_four이라는 변수에 phone_number의 마지막 4자리 수만 인덱싱해 대입
    return change_part + last_four # change_part와 last_four를 더해 문자열을 출력

print(solution("01033334444"))
print(solution("027778888"))