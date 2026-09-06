class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.data[key]
        if len(data) == 0:
            return ""
        if timestamp < data[0][0]:
            return ""
        if timestamp >= data[-1][0]:
            return data[-1][1]
        
        l = 0
        r = len(data) - 1
        while l < r:
            m = l + (r - l) // 2
            t, val = data[m]
            if timestamp == t:
                return val
            elif timestamp < t:
                r = m
            else:
                l = m + 1
        
        return data[l-1][1]

# l  m  r
# 10 20 30

# 15