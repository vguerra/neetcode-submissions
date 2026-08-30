class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][1] < temp:
                prev_idx, _ = stack.pop()
                result[prev_idx] = idx - prev_idx
            stack.append((idx, temp))

        return result
