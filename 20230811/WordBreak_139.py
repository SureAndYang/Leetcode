#!/usr/bin/python3

""" Medium: Word Break
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a
space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Node:
    def __init__(self, char: str | None):
        self.end = False
        self.child = {}


class Solution:
    def __init__(self):
        self.searchTree = None
        self.only_header = set()


    def search(self, s, root):
        for i, char in enumerate(s):
            if char not in root.child:
                break
            root = root.child[char]
            if root.end and (i == len(s) - 1 or self.search(s[i+1:], self.searchTree)):
                return True
        return False


    def loadDict(self, wordDict):
        self.searchTree = Node(None)
        header, body = set(), set()
        for word in sorted(wordDict):
            if self.search(word, self.searchTree):
                # Trick1: If a longer word can be represented by existing words, remove that word.
                # Because in this solution, more words with same prefix always mean more recursion
                # combination.
                continue
            root = self.searchTree
            for i, char in enumerate(word):
                if i == 0:
                    header.add(char)
                else:
                    body.add(char)
                if char not in root.child:
                    root.child[char] = Node(char)
                root = root.child[char]
            root.end = True
        self.only_header = header - body


    def cutString(self, s):
        strings = []
        start = 0
        for i, char in enumerate(s):
            if i > 1 and char in self.only_header:
                strings.append(s[start:i])
                start = i
        strings.append(s[start:])

        # Search from the shorter substrings.
        return sorted(strings, key=len)


    # Runtime 92.36%, Memory 5.12%.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.loadDict(wordDict)

        # If a character only existed as 'leading character', we can cut the string here.
        for s in self.cutString(s):
            if not self.search(s, self.searchTree):
                return False
        return True

class Solution_2:

    # [TODO] ] DP! Runtime 99.91%, Memory 97.29% as the author said.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max(map(len, wordDict))  # The maximum length of a word in the dictionary

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1): # Only consider words could fit.
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
