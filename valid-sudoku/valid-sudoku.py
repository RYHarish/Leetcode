class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(board):
            j = 0
            track = {}
            while j < len(board):
                if board[i][j] in track:
                    return False
                elif (board[i][j] != '.'):
                    track[board[i][j]] = 1
                j += 1
            i += 1
        
        i = 0
        j = 0
        while j < len(board):
            track = {}
            i = 0
            while i < len(board):
                if board[i][j] in track:
                    return False
                elif (board[i][j] != '.'):
                    track[board[i][j]] = 1
                i += 1
            j += 1
            
        k=0
        i=0
        j=0
        while k<3:
            c = 0
            while c<3:
                i = 3 * k
                j = 3 * c
                track = {}
                while (i< (k+1)*3):
                    while j < (c+1)*3:
                        if board[i][j] in track:
                            return False
                        elif (board[i][j] != '.'):
                            track[board[i][j]] = 1
                        j+=1
                    i+=1
                    j=c*3
                c+=1
            k+=1
                    
        return True
                