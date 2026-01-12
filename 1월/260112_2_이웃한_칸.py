def solution(board, h, w):
    answer = 0

    dh = [-1,0,1,0]
    dw = [0,1,0,-1]
    color = board[h][w]

    for i in range(4):
        check_h = h + dh[i]
        check_w = w + dw[i]
        if check_h < 0 or check_w < 0:
            continue
        if check_h >= len(board) or check_w >= len(board[0]):
            continue
        if color == board[check_h][check_w]:
            answer += 1

    return answer

print(solution([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]], 1, 1))
# print(solution([["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]], 0, 1))