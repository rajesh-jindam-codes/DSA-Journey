from collections import defaultdict
def groupedAnagram(strs):
    groups=defaultdict(list)
    for word in strs:
        key="".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupedAnagram(strs))