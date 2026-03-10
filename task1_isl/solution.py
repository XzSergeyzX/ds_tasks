import sys
from typing import List, Tuple


def flood_fill(grid: List[List[int]], start_r: int, start_c: int) -> None:
    """Flood-fill one island using an explicit stack."""
    rows = len(grid)
    cols = len(grid[0])
    stack: List[Tuple[int, int]] = [(start_r, start_c)]

    # Mark the starting cell as visited immediately
    grid[start_r][start_c] = 0

    while stack:
        r, c = stack.pop()

        # Check valid 4-directional neighbors before pushing them
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 0
                stack.append((nr, nc))


def count_islands(grid: List[List[int]]) -> int:
    """Count the number of islands in the grid."""
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                islands += 1
                flood_fill(grid, r, c)

    return islands


def main() -> None:
    """Read input from stdin and print the number of islands."""
    data = sys.stdin.read().split()
    if not data:
        return

    m = int(data[0])
    n = int(data[1])

    grid: List[List[int]] = []
    idx = 2

    for _ in range(m):
        row = [int(x) for x in data[idx:idx + n]]
        grid.append(row)
        idx += n

    print(count_islands(grid))


if __name__ == "__main__":
    main()