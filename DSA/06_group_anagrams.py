inp =["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    anangrams = {}
    for word in strs:
        anangrams[tuple(sorted(word))] = anangrams[tuple(sorted(word))] + [word] if tuple(sorted(word)) in anangrams else [word]
    
    return list(anangrams.values())


print(groupAnagrams(inp))
