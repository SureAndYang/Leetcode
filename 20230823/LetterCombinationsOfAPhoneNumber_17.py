#!/usr/bin/python3

""" Medium: Letter Combinations of a Phone Number.
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that
the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does
not map to any letters.
"""

class Solution:
    num_dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


    """Runtime 79.72%, Memory 51.87%"""
    def letterCombinations(self, digits: str) -> List[str]:
        # Recursive.
        if not digits:
            return []
        if len(digits) == 1:
            return list(self.num_dict[digits[0]])

        """Through testing, c+s is better than '{}{}'.format(c, s)"""
        return [c + s
                for s in self.letterCombinations(digits[1:]) for c in self.num_dict[digits[0]]]
