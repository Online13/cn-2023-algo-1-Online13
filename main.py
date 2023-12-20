"""
author = RATIARIVELO Nekena Rayane
version = 1.0.0
"""


class Solver:
    children_data: dict[str, tuple[str]]
    candy_data: dict[str, int]

    def __init__(self, children_data, candy_data):
        self.candy_data = candy_data
        self.children_data = children_data

    def solve(self):
        solution = {}

        for children in self.children_data.keys():
            solution[children] = {}
            for candy in self.children_data[children]:
                if self.candy_data[candy] == 0:
                    continue
                solution[children][candy] = 1
                self.candy_data[candy] -= 1
        return solution


if __name__ == "__main__":
    children_data = {
        "Alice": ("Chocolat", "Guimauve"),
        "Bob": ("Caramel", "Fruits"),
        "Charlie": ("Chocolat", "Caramel"),
    }

    candy_data = {
        "Chocolat": 10,
        "Caramel": 8,
        "Guimauve": 5,
        "Fruits": 6,
    }

    solver = Solver(children_data, candy_data)
    print(solver.solve())
    # print(len(solver.solutions), solver.solutions[1])
