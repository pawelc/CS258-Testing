# CHALLENGE PROBLEM: 
#
# Use your check_sudoku function as the basis for solve_sudoku(): a
# function that takes a partially-completed Sudoku grid and replaces
# each 0 cell with a number in the range 1..9 in such a way that the
# final grid is valid.
#
# There are many ways to cleverly solve a partially-completed Sudoku
# puzzle, but a brute-force recursive solution with backtracking is a
# perfectly good option. The solver should return None for broken
# input, False for inputs that have no valid solutions, and a valid
# 9x9 Sudoku grid containing no 0 elements otherwise. In general, a
# partially-completed Sudoku grid does not have a unique solution. You
# should just return some member of the set of solutions.
#
# A solve_sudoku() in this style can be implemented in about 16 lines
# without making any particular effort to write concise code.

# solve_sudoku should return None
ill_formed = [[5,3,4,6,7,8,9,1,2],
              [6,7,2,1,9,5,3,4,8],
              [1,9,8,3,4,2,5,6,7],
              [8,5,9,7,6,1,4,2,3],
              [4,2,6,8,5,3,7,9],  # <---
              [7,1,3,9,2,4,8,5,6],
              [9,6,1,5,3,7,2,8,4],
              [2,8,7,4,1,9,6,3,5],
              [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return valid unchanged
valid = [[5,3,4,6,7,8,9,1,2],
         [6,7,2,1,9,5,3,4,8],
         [1,9,8,3,4,2,5,6,7],
         [8,5,9,7,6,1,4,2,3],
         [4,2,6,8,5,3,7,9,1],
         [7,1,3,9,2,4,8,5,6],
         [9,6,1,5,3,7,2,8,4],
         [2,8,7,4,1,9,6,3,5],
         [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return False
invalid = [[5,3,4,6,7,8,9,1,2],
           [6,7,2,1,9,5,3,4,8],
           [1,9,8,3,8,2,5,6,7],
           [8,5,9,7,6,1,4,2,3],
           [4,2,6,8,5,3,7,9,1],
           [7,1,3,9,2,4,8,5,6],
           [9,6,1,5,3,7,2,8,4],
           [2,8,7,4,1,9,6,3,5],
           [3,4,5,2,8,6,1,7,9]]

# solve_sudoku should return a 
# sudoku grid which passes a 
# sudoku checker. There may be
# multiple correct grids which 
# can be made from this starting 
# grid.
easy = [[2,9,0,0,0,0,0,7,0],
        [3,0,6,0,0,8,4,0,0],
        [8,0,0,0,4,0,0,0,2],
        [0,2,0,0,3,1,0,0,7],
        [0,0,0,0,8,0,0,0,0],
        [1,0,0,9,5,0,0,6,0],
        [7,0,0,0,9,0,0,0,1],
        [0,0,1,2,0,0,3,0,6],
        [0,3,0,0,0,0,0,5,9]]

# Note: this may timeout 
# in the Udacity IDE! Try running 
# it locally if you'd like to test 
# your solution with it.
# 
hard = [[1,0,0,0,0,7,0,9,0],
         [0,3,0,0,2,0,0,0,8],
         [0,0,9,6,0,0,5,0,0],
         [0,0,5,3,0,0,9,0,0],
         [0,1,0,0,8,0,0,0,2],
         [6,0,0,0,0,4,0,0,0],
         [3,0,0,0,0,0,0,1,0],
         [0,4,0,0,0,0,0,0,7],
         [0,0,7,0,0,0,3,0,0]]

def getColumn(matrix,col):
        return map(lambda row: row[col],matrix)

def check_sudoku(grid):
    if len(grid) != 9:
        return None
    for row in grid:
        if not all(map(lambda e: range(0,10).count(e) >= 1,row)):
            return None
        if len(row) != 9:
            return None
    
    
    for i in range(0,9):
        if not all(map(lambda e: grid[i].count(e) <= 1,range(1,10))):
            return False
        if not all(map(lambda e: getColumn(grid,i).count(e) <= 1,range(1,10))):
            return False
    
    def subMatrixAsRow(matrix,i,j):
        l=[]
        for m in range(3):
            for n in range(3):
                l.append(matrix[i+m][j+n])
        return l
            
    for i in range(0,8,3):
        for j in range(0,8,3):
            if not all(map(lambda e: subMatrixAsRow(grid,i,j).count(e) <= 1,range(1,10))):
                return False
        
    return True

def solve_sudoku (grid):
    import copy
    ret = check_sudoku(grid)
    if not ret:
        return ret
    
    def getZeroPos(matrix):
        return [(i,j) for i,row in enumerate(matrix) for j, x in enumerate(row) if x == 0]
    
    def validNums(matrix,z):
        valid=set(range(1,10))
        valid-=set(matrix[z[0]])
        valid-=set(getColumn(matrix,z[1]))
        return valid
        
    
    allZeros = getZeroPos(grid)
    def check(zeros, index,matrix):
        if len(zeros) <= index:
            if check_sudoku(matrix):
                return matrix
            else:
                return False            
        
        z = zeros[index]
        vnums=validNums(matrix,z)
        for i in vnums:
            copyM=copy.deepcopy(matrix)
            copyM[z[0]][z[1]]=i
            valid = check_sudoku(copyM)
            if valid:
                ret=check(zeros,index+1,copyM)
                if ret:
                    return ret
    
    if not allZeros:
        if check_sudoku(grid):
            return grid
        else:
            return None
    
    for i in range(1,10):
        grid[allZeros[0][0]][allZeros[0][1]]=i
        valid = check_sudoku(grid)
        if valid:
            ret=check(allZeros,1,grid)
            if ret:
                return ret
    return False

s=solve_sudoku(easy)
print s
print check_sudoku(s)
