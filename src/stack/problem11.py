def soultion(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return int(not stack)


# # 예시 1
# s = "baabaa"
# print(solution(s))  # 출력: 1 (모두 짝지어 제거 가능)

# # 예시 2
# s = "cdcd"
# print(solution(s))  # 출력: 0 (모두 짝지어 제거 불가능)