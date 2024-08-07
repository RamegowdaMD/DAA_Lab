global N
N = int(input("Enter the number queens"))


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end=" ")
        print()

        
def backtrack(row , col,board):
    for i in range(col):
        if board[row][i] ==1: #col row wise
            return False
    for i, j in zip(range(row,-1,-1) , range(col,-1,-1)):
        #diagonally
        if board[i][j] == 1:
            return False
    for i , j in zip(range(row,N,-1),range(col,-1,-1)):
        #diagonally
        if board[i][j]==1:
            return False
    return True


def solveNQutil(board,col):
    if col>=N:
        return True
    for i in range(N):
        if backtrack(i ,col,board):
            board[i][col]=1
            if solveNQutil(board , col+1) == True:
                return True
            board[i][col]=0
    return False


def solveNQ():
	board = [[0 for i in range(N)] for j in range(N)]
	if solveNQutil(board, 0) == False:
		print ("Solution does not exist")
		return False
	printSolution(board)
	return True
solveNQ()
