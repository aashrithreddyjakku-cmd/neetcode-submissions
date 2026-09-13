class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen=set()

            for j in range(9):
                x=board[i][j]

                if x == ".":
                    continue
                if x in seen:
                    return False
                seen.add(x)
        
        for j in range(9):
            seen=set()

            for i in range(9):
                x=board[i][j]

                if x==".":
                    continue
                if x in seen:
                    return False
                seen.add(x)

        for row_start in range(0,9,3):
            for column_start in range(0,9,3):

                seen = set()

                for i in range(3):
                    for j in range(3):
                        x=board[row_start+i][column_start+j]
                        if x==".":
                         continue
                        if x in seen:
                            return False
                        seen.add(x)
        
        return True
