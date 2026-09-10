class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            match op:
                case "+":
                    x, y = record[-2], record[-1]
                    record.append(x + y)
                case "D":
                    x = record[-1]
                    record.append(2 * x)
                case "C":
                    record.pop()
                case _:
                    record.append(int(op))
    
        return sum(record)
        