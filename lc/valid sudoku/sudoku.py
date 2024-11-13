
def isValidSudoku(board):
    # row check duplicatre
    for row in range(len(board)):
        seen = []
        for col in range(len(board)):
            currNum = board[row][col]
            if currNum != ".":
                if currNum not in seen:
                    seen.append(currNum)
                else:
                    return False
    # col check duplicate
    for col in range(len(board)):
        seen = []
        for row in range(len(board)):
            currNum = board[row][col]
            if currNum != ".":
                if currNum not in seen:
                    seen.append(currNum)
                else:
                    return False
    # check 3x3
    row = 0
    while row < len(board) - 3 + 1:
        col = 0
        while col < len(board) - 3 + 1:
            seen = []
            if board[row][col] != ".":
                if board[row][col] not in seen:
                    seen.append(board[row][col])
                else:
                    return False
            if board[row][col + 1] != ".":
                if board[row][col + 1] not in seen:
                    seen.append(board[row][col + 1])
                else:
                    return False
            if board[row][col + 2] != ".":
                if board[row][col + 2] not in seen:
                    seen.append(board[row][col + 2])
                else:
                    return False

            if board[row + 1][col] != ".":
                if board[row + 1][col] not in seen:
                    seen.append(board[row + 1][col])
                else:
                    return False
            if board[row + 1][col + 1] != ".":
                if board[row + 1][col + 1] not in seen:
                    seen.append(board[row + 1][col + 1])
                else:
                    return False
            if board[row + 1][col + 2] != ".":
                if board[row + 1][col + 2] not in seen:
                    seen.append(board[row + 1][col + 2])
                else:
                    return False
            
            if board[row + 2][col] != ".":
                if board[row + 2][col] not in seen:
                    seen.append(board[row + 2][col])
                else:
                    return False
            if board[row + 2][col + 1] != ".":
                if board[row + 2][col + 1] not in seen:
                    seen.append(board[row + 2][col + 1])
                else:
                    return False
            if board[row + 2][col + 2] != ".":
                if board[row + 2][col + 2] not in seen:
                    seen.append(board[row + 2][col + 2])
                else:
                    return False
            col += 3
        row += 3
    return True

