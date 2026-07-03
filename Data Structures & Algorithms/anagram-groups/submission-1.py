class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def freq(word:str) -> Tuple[int]:
            counts = [0] * 26
            for c in word:
                counts[ord(c) - 97] += 1
            return tuple(counts)

        anagrams = defaultdict(list)
        for word in strs:
            anagrams[freq(word)].append(word)
        return list(anagrams.values())
        