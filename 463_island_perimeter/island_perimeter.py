import pytest


class NoLandError(Exception):
    pass


class IslandPerimeter(object):
    def __init__(self):
        self.CELL_ADJACENCY = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    @staticmethod
    def find_land(ocean):
        for row_idx, row in enumerate(ocean):
            for col_idx, cell in enumerate(row):
                if cell:
                    return row_idx, col_idx
        raise NoLandError('No land present in provided ocean.')

    @staticmethod
    def is_land(ocean, cell):
        return IslandPerimeter.is_valid_cell(ocean, cell) and ocean[cell[0]][cell[1]]

    @staticmethod
    def is_valid_cell(ocean, cell):
        return 0 <= cell[0] <= len(ocean) - 1 and 0 <= cell[1] <= len(ocean[cell[0]]) - 1

    def island_perimeter(self, ocean):
        if ocean is None or len(ocean) == 0:
            raise TypeError('Invalid input for ocean.')
        land_row, land_col = IslandPerimeter.find_land(ocean)
        land_queue = [(land_row, land_col)]
        visited = set()
        perimeter = 0
        while land_queue:
            cell = land_queue.pop(0)
            visited.add(cell)
            for adjacency in self.CELL_ADJACENCY:
                next_cell = (cell[0] + adjacency[0], cell[1] + adjacency[1])
                if next_cell not in visited and next_cell not in land_queue:
                    if IslandPerimeter.is_land(ocean, next_cell):
                        land_queue.append(next_cell)
                    else:
                        perimeter += 1
        return perimeter


class Solution(object):
    @staticmethod
    def islandPerimeter(grid):
        ip = IslandPerimeter()
        return ip.island_perimeter(grid)


class TestIslandPerimeter(object):
    def test_find_land(self):
        assert IslandPerimeter.find_land([[0, 0, 0, 1]]) == (0, 3)
        assert IslandPerimeter.find_land([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0]]) == (2, 2)
        with pytest.raises(NoLandError):
            IslandPerimeter.find_land([[0, 0, 0, 0], [0, 0, 0, 0]])

    def test_island_perimeter(self):
        ocean = [[1, 0]]
        assert Solution.islandPerimeter(ocean) == 4
        ocean = [[1, 1], [1, 1]]
        assert Solution.islandPerimeter(ocean) == 8
        ocean = [[0, 1], [0, 1]]
        assert Solution.islandPerimeter(ocean) == 6
        ocean = [[0, 1, 0],
                 [1, 1, 1],
                 [0, 1, 0]]
        assert Solution.islandPerimeter(ocean) == 12
        ocean = [[0, 1, 0, 0],
                 [1, 1, 1, 0],
                 [0, 1, 0, 0],
                 [1, 1, 0, 0]]
        assert Solution.islandPerimeter(ocean) == 16
