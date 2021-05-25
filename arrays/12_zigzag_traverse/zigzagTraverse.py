# O(n) time space, n -> total no. of elements in the 2D arr
def zigzagTraverse(arr):
    height = len(arr) - 1
    width = len(arr[0]) - 1
    row, col = 0, 0
    result = []
    goingDown = True
    while not isOutofbounds(row, col, height, width):
        result.append(arr[row][col])
        if goingDown:
            # if element in perimeter
            if col == 0 or row == height:
                goingDown = False
                if row == height:
                    col += 1
                else:
                    row += 1
            # if element not in perimeter
            else:
                row += 1
                col -= 1
        else:
            # if element in perimeter
            if row == 0 or col == width:
                goingDown = True
                if col == width:
                    row += 1
                else:
                    col += 1
            # if element not in perimeter
            else:
                row -= 1
                col += 1
                
    return result
                

def isOutofbounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width

arr = [
       [1, 3, 4, 10],
       [2, 5, 9, 11],
       [6, 8, 12, 15],
       [7, 13, 14, 16]
       ]
print(zigzagTraverse(arr))
