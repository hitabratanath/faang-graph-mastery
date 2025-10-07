class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        source = "0000"
        if source in deadends: return -1
        deadends = set(deadends)

        n = len(deadends)
        queue = deque([(0, source)])
        visited = set()

        def getNextCombination(combination, wheel, delta):
            digits = list(combination)
            digits[wheel] = str((int(digits[wheel]) + delta) % 10)
            return "".join(digits) 

        while queue:
            turns, current = queue.popleft()
            if current == target: return turns

            for delta in [1, -1]:
                for wheel in range(4):
                    next_combination = getNextCombination(current, wheel, delta)
                    if next_combination not in deadends and next_combination not in visited:
                        visited.add(next_combination)
                        queue.append((turns + 1, next_combination))
        
        return -1
        