def solution(s) :
    answer = 0

    n = len(s)
    for i in range(n):
        stack = []
        for j in range(n):
            
            # open compare -> push
            c = s[(i + j) % n]
            if c == "(" or c == "[" or c == "{" :
                stack.append(c)

            else:
                if not stack:
                    break
            
                 # close compare -> pop
                if c == ")" and stack[-1] == "(" :
                    stack.pop()

                elif c == "]" and stack[-1] == "[":
                    stack.pop()

                elif c == "}" and stack[-1] == "{":
                    stack.pop()

                else : 
                    break
        else:
            if not stack:
                answer += 1
    return answer

            

# s = "[](){}"
# print(solution(s))  # 출력: 3

# s = "}]()[{"
# print(solution(s))  # 출력: 2

# s = "[)(]"
# print(solution(s))  # 출력: 0

# s = "}}}"
# print(solution(s))  # 출력: 0
