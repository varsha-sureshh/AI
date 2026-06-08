from queue import PriorityQueue

class State:
    def __init__(self, left_missionaries, left_cannibals, boat, parent=None):
        self.left_missionaries = left_missionaries
        self.left_cannibals = left_cannibals
        self.boat = boat
        self.parent = parent

    def is_valid(self):
        # Check for negative values
        if self.left_missionaries < 0 or self.left_cannibals < 0:
            return False
        if 3 - self.left_missionaries < 0 or 3 - self.left_cannibals < 0:
            return False

        # Missionaries should not be outnumbered
        if (self.left_missionaries != 0 and self.left_missionaries <
                self.left_cannibals):
            return False
        if ((3 - self.left_missionaries) != 0 and
                (3 - self.left_missionaries) < (3 - self.left_cannibals)):
            return False

        return True

    def is_goal(self):
        return self.left_missionaries == 0 and self.left_cannibals == 0

    def __lt__(self, other):
        return False
        # Required for PriorityQueue

    def __eq__(self, other):
        return (self.left_missionaries == other.left_missionaries and
                self.left_cannibals == other.left_cannibals and
                self.boat == other.boat)

    def __hash__(self):
        return hash((self.left_missionaries, self.left_cannibals, self.boat))

    def successors(self):
        successors = []

        if self.boat == 'left':
            for i in range(3):
                for j in range(3):
                    if 1 <= i + j <= 2:
                        new_state = State(
                            self.left_missionaries - i,
                            self.left_cannibals - j,
                            'right',
                            self
                        )
                        if new_state.is_valid():
                            successors.append(new_state)
        else:
            for i in range(3):
                for j in range(3):
                    if 1 <= i + j <= 2:
                        new_state = State(
                            self.left_missionaries + i,
                            self.left_cannibals + j,
                            'left',
                            self
                        )
                        if new_state.is_valid():
                            successors.append(new_state)

        return successors

    def path(self):
        path = []
        current = self

        while current:
            path.append(current)
            current = current.parent

        return path[::-1]


def best_first_search():
    initial_state = State(3, 3, 'left')
    frontier = PriorityQueue()
    frontier.put((0, initial_state))
    explored = set()

    while not frontier.empty():
        _, state = frontier.get()

        if state.is_goal():
            return state.path()

        explored.add(state)

        for successor in state.successors():
            if successor not in explored:
                frontier.put((len(successor.path()), successor))

    return None


def print_solution(solution):
    for i, state in enumerate(solution):
        print("Step", i, ":")
        print("Left side:", state.left_missionaries, "missionaries and",
              state.left_cannibals, "cannibals")
        print("Boat is on the", state.boat, "side.")
        print("Right side:", 3 - state.left_missionaries, "missionaries and",
              3 - state.left_cannibals, "cannibals")
        print()


if __name__ == "__main__":
    solution = best_first_search()

    if solution:
        print("Solution found:\n")
        print_solution(solution)
    else:
        print("No solution found.")
