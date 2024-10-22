import math 

def solution(mod1, mod2, max_range):

    count1 = max_range // mod1

    temp = (mod1 * mod2) // math.gcd(mod1, mod2)

    count2 = max_range // temp

    return count1 - count2

# 속도 테스트까지 통과한 코드 ( 반복문 x )

# 정확도만 있고, 속도는 느려서 실패한 코드

def solution2(mod1, mod2, max_range):
    count = 0
    
    # 1 이상 max_range 이하의 수를 검사
    for num in range(1, max_range + 1):
        if num % mod1 == 0 and num % mod2 != 0:
            count += 1
            
    return count

# 테스트
print(solution2(4, 3, 20))  # 결과: 4
print(solution2(3, 4, 20))  # 결과: 5
