class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def sign(x: int) -> int:
            return 1 if x >= 0 else -1

        stack = []
        for asteroid in asteroids:
            stack.append(asteroid)
            collisioned = True
            while len(stack) > 1 and collisioned:
                ast1 = stack.pop()
                ast2 = stack.pop()
                if sign(ast1) == sign(ast2) or (sign(ast1) == 1 and sign(ast2) == -1):
                    stack.append(ast2)
                    stack.append(ast1)
                    collisioned = False
                elif abs(ast1) > abs(ast2):
                    stack.append(ast1)
                elif ast1 + ast2 == 0:
                    continue
                else:
                    stack.append(ast2)

        return stack
        