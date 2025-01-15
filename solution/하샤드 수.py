def solution(x):  
    digit_sum = sum(int(digit) for digit in str(x))  
    
    if digit_sum == 0:    
       
        return False  
    
    return x % digit_sum == 0 

print(solution(10)) 
print(solution(11)) 
print(solution(12)) 
print(solution(13)) 