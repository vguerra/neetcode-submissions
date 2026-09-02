class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        print(rows, cols)
        def at(pos: int) -> int:
            col = pos % cols
            row = (pos - col) // cols
            return matrix[row][col]
        
        l = 0
        r = rows * cols - 1

        while l <= r:
            m = l + (r - l) // 2
            m_val = at(m)
            if m_val == target:
                return True
            elif target < m_val:
                r = m - 1
            else:
                l = m + 1
        return False
