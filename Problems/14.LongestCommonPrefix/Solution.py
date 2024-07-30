from typing import List

# Submission Detail - 

'''
class TrieNode:
    def __init__(self):
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def set_cache

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children 
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        for word in strs:
            if len(word) == 0:
                return ""