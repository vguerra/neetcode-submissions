class Solution:
    def decodeString(self, s: str) -> str:
        ans = []
        stack_l = []
        stack_n = []

        i = 0
        while i < len(s):
            c = s[i]
            match c:
                case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
                    start = i
                    while s[i].isdigit():
                        i += 1
                    repeats = int(s[start:i])
                    stack_n.append(repeats)
                    print("found repeats: ", repeats)
                case "]":
                    sub_str = []
                    while stack_l and stack_l[-1] != '[':
                        sub_str.append(stack_l.pop())
                    if stack_l:
                        stack_l.pop()
                    times = stack_n.pop()
                    print("we need to repeat ", sub_str, " times ", times)
                    stack_l.append("".join(reversed(sub_str)) * times)
                    i += 1
                case _:
                    stack_l.append(c)
                    i += 1
        print(stack_l)
        print(ans)
        return "".join(stack_l)
    