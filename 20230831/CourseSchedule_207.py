#!/usr/bin/python3

""" Medium: Course Schedule
"""


class Solution:
    """Runtime 7.77%, Memory 5.22% (105.1Mb). It's not sufficient, but a valid solution. We should
    find the reasons and try to fix them.
    """
    def canFinish_1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(start, seen):
            if start not in dependency or start in success:
                return True
            if start in seen:
                return False
            seen.add(start)
            for child in dependency[start]:
                if not dfs(child, seen.copy()):
                    return False
            success.add(start)
            return True

        dependency = defaultdict(list)
        for course, dep in prerequisites:
            dependency[course].append(dep)

        success = set()
        for course in dependency:
            seen = set()
            if not dfs(course, seen):
                return False
        return True


    """Runtime 7.40%, Memory 5.22% (50.68Mb), reduce the memory by half successfully, but this is
    still very inefficient.

    Improvements:
        1. Data type of 'seen' from set to list, reduce memory.
    """
    def canFinish_2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def recur(start: int, seen: List[int], success: set) -> bool:
            if start in success or start not in pre:
                return True
            if seen[start]:
                return False
            seen[start] = True
            for child in pre[start]:
                """Remove the 'copy' action can reduce time and memory greatly.

                Runtime 74.84%, Memory 11.92%, when `if not recur(child, seen, success):`
                """
                if not recur(child, seen[:], success):
                    """Sometime we truely need this copy, that is when we need to output a path, a
                    combination or sth similar"""
                    return False
            success.add(start)
            return True

        pre = defaultdict(list)
        for pair in prerequisites:
            pre[pair[0]].append(pair[1])

        success = set()
        for n in range(numCourses):
            seen = [False] * numCourses
            if not recur(n, seen, success):
                return False
        return True


    """Runtime 77.37%, Memory 34.04%. Almost same thought with solution 1 and 2.

    Improvements:
        1. Data type of 'depends' from dict to list[list], reduce memory.
        2. Data type of 'success' from set to list, reduce memory.
        3. Make variable 'visited' global, remove 'copy', reduce time and memory.
    """
    def canFinish_3(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Find circle in graph.
        def dfs(node, visited, success):
            if success[node]:
                return True
            if visited[node]:
                return False

            visited[node] = True
            for child in depends[node]:
                if not dfs(child, visited, success):
                    return False
            success[node] = True
            return True

        success = [False] * numCourses
        visited = [False] * numCourses

        depends = [[] for _ in range(numCourses)]
        for course, depend in prerequisites:
            """ Runtime 69.59%, Memory 56.32%. Handling special cases reduces much memory in
            Leetcode.
            The runtime and memory change randomly in a certain range. Sometimes runtime goes to
            99%, but memory goes down to 37%.

            if course == depend: # When if [0, 0], thus 0 depends on 0, return False.
                return False
            """
            depends[course].append(depend)

        for n in range(numCourses):
            if not dfs(n, visited, success):
                return False
        return True


    """Runtime 96.47%/100%, Memory 48.57%/56.3%. Let visited having more status, we can remove
    success then.
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Find circle in graph.
        def dfs(node, visited):
            if visited[node] == 2:
                return True
            if visited[node] == 1:
                return False

            visited[node] = 1
            for child in depends[node]:
                if not dfs(child, visited):
                    return False
            visited[node] = 2
            return True

        visited = [0] * numCourses

        depends = [[] for _ in range(numCourses)]
        for course, depend in prerequisites:
            if course == depend:
                return False
            depends[course].append(depend)

        for n in range(numCourses):
            if not dfs(n, visited):
                return False
        return True


    """Runtime 92.57%, Memory 60%. Let 'depends[node] = []' being empty represent 'success'."""
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Find circle in graph.
        def dfs(node, visited):
            if not depends[node]:
                return True
            if visited[node] == 1:
                return False

            visited[node] = 1
            for child in depends[node]:
                if not dfs(child, visited):
                    return False
            depends[node].clear()
            return True

        visited = [0] * numCourses

        depends = [[] for _ in range(numCourses)]
        for course, depend in prerequisites:
            if course == depend:
                return False
            depends[course].append(depend)

        for n in range(numCourses):
            if not dfs(n, visited):
                return False
        return True
