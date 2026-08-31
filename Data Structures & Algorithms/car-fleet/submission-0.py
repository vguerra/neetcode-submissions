class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort(reverse=True)

        stack = []
        for pos, speed in pos_speed:
            time = (target - pos) / speed
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)
        return len(stack)
        