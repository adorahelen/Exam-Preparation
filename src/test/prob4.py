# s = "abababab"

# def calculate(s):
#     n = len(s)
#     lps = [0] * n  # LPS 배열 초기화
#     length = 0  # LPS의 길이
#     i = 1  # 인덱스 초기화

#     while i < n:
#         if s[i] == s[length]:  # 현재 문자와 LPS의 끝 문자 비교
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length - 1]  # LPS 길이 업데이트
#             else:
#                 lps[i] = 0
#                 i += 1
#     return lps

# def solution(s):
#     n = len(s)
#     if n == 0:
#         return 0
#     lps = calculate(s)  # LPS 배열 계산
#     result = n - lps[-1]  # 주기 계산

#     # 주기 계산
#     if n % result == 0 and result != n:  # 전체 문자열 길이로 나누어 떨어지고, 주기가 전체 길이와 같지 않을 때
#         return n // result  # 주기 반환
#     else:
#         return n  # 주기가 없으므로 전체 길이를 반환

# # 테스트 예시
# output = solution(s)
# print(output)  # 주기 결과 출력

# "abababab" => 2 
# "abcabcabd" => 9 
# 둘다 안나오네
