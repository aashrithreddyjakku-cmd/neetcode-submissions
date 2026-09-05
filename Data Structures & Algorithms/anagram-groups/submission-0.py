class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)

        for x in strs:
            key="".join(sorted(x))
            group[key].append(x)
        
        return list(group.values())

    