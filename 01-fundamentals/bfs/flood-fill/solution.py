class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        original_color = image[sr][sc]
        queue = deque([(sr, sc)])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            x, y = queue.popleft()
            image[x][y] = color
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == original_color and image[nx][ny] != color:
                    queue.append((nx, ny))
        return image
        