import sys

# Part 1
def solut1():
    
    grid = [list(line.strip()) for line in sys.stdin.readlines()]
    rows = len(grid)
    cols = len(grid[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    ans = 0

    def check_for_papers(x, y):
        papers = 0
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < rows and 0 <= ny < cols: # within bounds
                if grid[nx][ny] == "@":
                    papers += 1
        return papers
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "@":
                papers_count = check_for_papers(i, j)
                if papers_count < 4:
                    ans += 1
    return ans

print(solut1())