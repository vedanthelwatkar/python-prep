"""
Longest Substring Without Repeating Characters
Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is charset size
"""

string = "abcfghsddea"

def longest_subs(s):
    """
    Returns the actual longest substring without repeating characters.
    Uses sliding window technique with a set.
    """
    char_set = set()
    left = 0
    start_ind = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_ind = left
    
    return s[start_ind:start_ind + max_len]

def lengthOfLongestSubs(s):
    """
    Returns the length of the longest substring without repeating characters.
    More efficient as it only tracks length, not the substring.
    """
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1 
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

print("Longest Substring:", longest_subs(string))
print("Length of Longest Substring:", lengthOfLongestSubs(string))
