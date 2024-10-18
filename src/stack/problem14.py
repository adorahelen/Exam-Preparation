def solution(n, k, cmd):
    deleted = []
    up = [i - 1 for i in range(n + 1)]
    down = [i + 1 for i in range(n)]

    k += 1

    for cmd_i in cmd:

        if cmd_i.startswith("C"):
            deleted.append(k)

            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if down[k] >= n else down[k]

        elif cmd_i.startswith("Z"):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore

        else:
            action, num = cmd_i.split()
            if action == "U":
                for _ in range(int(num)):
                    k = up[k]
            elif action == "D":
                for _ in range(int(num)):
                    k = down[k]

    answer = ["O"] * n

    for i in deleted:
        answer[i - 1] = "X"
    return "".join(answer)


# # 예시
# n = 8
# k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
# print(solution(n, k, cmd))  # 출력: "OOOOXOOO"