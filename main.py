"""
author = RATIARIVELO Nekena Rayane
version = 2.0.0
"""


class Solver:
    children_data: dict[str, tuple[str]]
    candy_data: dict[str, int]

    variables: dict[str, dict[str, int]]
    keys: list[tuple[str]]
    solutions: list[(dict[str, dict[str, int]], int)]
    max_satisfaction: int

    def __init__(self):
        self.candy_data = None
        self.children_data = None

        self.variables = None
        self.keys = None
        self.solutions = []
        self.max_satisfaction = 0

    def define(self, children_data: dict[str, tuple[str]], candy_data: dict[str, int]):
        self.candy_data = candy_data
        self.children_data = children_data

        self.variables = {
            children: {candy: 0 for candy in self.candy_data.keys()}
            for children in self.children_data.keys()
        }
        self.keys = [
            (children, candy)
            for children in self.children_data
            for candy in self.children_data[children]
        ]

    def get_domaine(self, children, candy):
        if candy in self.children_data[children]:
            return list(range(self.candy_data[candy], 0, -1))
        return [0]

    def verify_constraint(self, value, state, children, candy):
        if candy in self.children_data[children]:
            max_candy = self.candy_data[candy]
            if value < 1:
                return False
            if value > max_candy:
                return False
            if sum([state[children][_candy] for _candy in self.candy_data]) > max_candy:
                return False

        return True

    def compute_satisfaction(self, state: dict[str, dict[str, int]]):
        total = [sum(state[children].values()) for children in state.keys()]
        # because the rightness constraint should be verified,
        # we can assume that it should be unique
        return total[0]

    def is_right_for_all_children(self, state: dict[str, dict[str, int]]):
        total = [sum(state[children].values()) for children in state.keys()]
        return len(set(total)) == 1

    def solve(self, state=None, current=0):
        current_state = None
        if current == 0:
            current_state = {
                children: {candy: 0 for candy in self.candy_data.keys()}
                for children in self.children_data.keys()
            }
        else:
            current_state = {
                children: {
                    candy: state[children][candy] for candy in self.candy_data.keys()
                }
                for children in self.children_data.keys()
            }

        if current == len(self.keys):
            if self.is_right_for_all_children(current_state):
                satisfaction = self.compute_satisfaction(current_state)
                if satisfaction > self.max_satisfaction:
                    self.max_satisfaction = satisfaction
                    del self.solutions
                    self.solutions = [current_state]
                elif satisfaction == self.max_satisfaction:
                    self.solutions.append(current_state)
            return

        children, candy = self.keys[current]
        for value in self.get_domaine(candy=candy, children=children):
            if self.verify_constraint(
                value=value, state=current_state, children=children, candy=candy
            ):
                current_state[children][candy] = value
                self.solve(current=current + 1, state=current_state)
                current_state[children][candy] = 0
            else:
                return None

    def summary_solution(self):
        for solution in self.solutions:
            [
                print(
                    children,
                    "=",
                    {
                        candy: solution[children][candy]
                        for candy in self.candy_data.keys()
                    },
                )
                for children in self.children_data.keys()
            ]
            print()
        print("Possible solution =", len(self.solutions))


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

    solver = Solver()
    solver.define(children_data, candy_data)
    solver.solve(None, 0)
    solver.summary_solution()
