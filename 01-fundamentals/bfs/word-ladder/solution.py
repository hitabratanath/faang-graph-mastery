class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)  # for O(1) lookup
        if endWord not in word_set:
            return 0  # no path possible

        queue = deque([(beginWord, 1)])  # start distance = 1 (include beginWord)
        visited = set([beginWord])
        N = len(beginWord)

        while queue:
            word, dist = queue.popleft()

            if word == endWord:
                return dist

            for i in range(N):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue  # skip same letter
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        queue.append((next_word, dist + 1))
        
        return 0
