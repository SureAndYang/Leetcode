#!/usr/bin/python3

""" Hard: Text Justification
Given an array of strings words and a width maxWidth, format the text such that each line has
exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line
. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a
line does not divide evenly between words, the empty slots on the left will be assigned more spaces
than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words
.

Note:
    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
"""

class Solution:
    """Runtime 7.57%, Memory 25.68%. A easy and straight solution."""
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        start_word, sen_len, res = 0, 0, []
        for i, cur in enumerate(words):
            if sen_len + len(cur) + (i - start_word - 1) >= maxWidth:
                # Adding current word will extend the max width.
                if i - start_word - 1 == 0:
                    sen = words[start_word] + ' ' * (maxWidth - sen_len)
                else:
                    blanks, mod = divmod(maxWidth - sen_len, i - start_word - 1)
                    if mod == 0:
                        sen = (' ' * blanks).join(words[start_word: i])
                    else:
                        sen = (' ' * (blanks + 1)).join(words[start_word: start_word + mod]) + \
                        ' ' * (blanks + 1) + (' ' * blanks).join(words[start_word + mod: i])
                res.append(sen)
                start_word, sen_len = i, len(cur)
            else:
                sen_len += len(cur)
        if start_word < len(words):
            res.append(' '.join(words[start_word:]) + ' ' * (maxWidth - sen_len - len(words) +
                                                             start_word + 1))
        return res


    """Runtime 55.77%, Memory 64.76%. Proper variables can reduce duplicated math caculations."""
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        start_word, left_len, gap_num, res = 0, maxWidth, -1, []
        for i, cur in enumerate(words):
            if left_len - gap_num <= len(cur):
                # Adding current word will extend the max width.
                if gap_num == 0:
                    sen = words[start_word] + ' ' * left_len
                else:
                    blanks, mod = divmod(left_len, gap_num)
                    if mod == 0:
                        sen = (' ' * blanks).join(words[start_word: i])
                    else:
                        sen = (' ' * (blanks + 1)).join(words[start_word: start_word + mod]) + \
                        ' ' * (blanks + 1) + (' ' * blanks).join(words[start_word + mod: i])
                res.append(sen)
                start_word, left_len, gap_num = i, maxWidth - len(cur), 0
            else:
                left_len -= len(cur)
                gap_num += 1
        if start_word < len(words):
            res.append(' '.join(words[start_word:]) + ' ' * (left_len - gap_num))
        return res
