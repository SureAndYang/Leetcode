#!/usr/bin/python3

""" Hard: Frog Jump
A frog is crossing a river. The river is divided into some number of units, and at each unit, there
may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can
cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes
the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog
can only jump in the forward direction.
"""

class Solution:
    """Runtime 48.68%, Memory 71.47%"""
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 2:
            return stones[1] - stones[0] == 1

        from_stone = defaultdict(set)
        # First step is 1. The second step is 1 or 2 (0 is meaningless for now).
        from_stone[2] = {1}
        from_stone[3] = {1}

        for i in range(2, len(stones)):
            for start in from_stone[stones[i]]:
                for gap in range(max(stones[i]-start-1, 1), stones[i]-start+2):
                    from_stone[stones[i] + gap].add(stones[i])
        return len(from_stone[stones[-1]]) > 0


    """Runtime 58.94%, Memory 71.86%"""
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) == 2:
            return stones[1] - stones[0] == 1

        jump_to = defaultdict(set)
        # First step is 1. The second step is 1 or 2 (0 is meaningless for now).
        jump_to[2] = {1}
        jump_to[3] = {1}

        for i in range(2, len(stones)):
            for start in jump_to[stones[i]]:
                gap = stones[i]-start
                """Replacing 'max(gap-1, 1)' with 'gap - 1 or 1' leads the improment on time."""
                for step in range(gap - 1 or 1, gap + 2):
                    jump_to[stones[i] + step].add(stones[i])
        return len(jump_to[stones[-1]]) > 0
