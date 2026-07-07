class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = {i : set() for i in range(9)}
        col_sets = {i : set() for i in range(9)}
        square_sets = {i : set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num in row_sets[i]:
                    return False
                row_sets[i].add(num)
                if num in col_sets[j]:
                    return False
                col_sets[j].add(num)
                square_idx = int((i // 3) * 3 + (j // 3))
                if num in square_sets[square_idx]:
                    return False
                square_sets[square_idx].add(num)

        return True


        