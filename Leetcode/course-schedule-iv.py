class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        incoming = [0] * (numCourses)
        precourses = defaultdict(set)
        
        for pre, course in prerequisites:
            graph[pre].append(course)
            precourses[course].add(pre)
            incoming[course] += 1


        queue = deque()
        for node in range(numCourses):
            if incoming[node] == 0:
                queue.append(node)

        while queue:
            pre = queue.popleft()

            for course in graph[pre]:
                precourses[course] |= precourses[pre]

                incoming[course] -= 1
                if incoming[course] == 0:
                    queue.append(course)

        ans = []
        for pre, course in queries:
            ans.append(pre in precourses[course])

        return ans