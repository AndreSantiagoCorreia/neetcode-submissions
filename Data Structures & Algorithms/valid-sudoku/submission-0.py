class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                entry = board[r][c]
                if entry == ".":
                    continue
                if entry in rows[r] or entry in cols[c] or entry in boxes[(r // 3, c // 3)]:
                    return False
                
                rows[r].add(entry)
                cols[c].add(entry)
                boxes[(r // 3, c // 3)].add(entry)

        return True