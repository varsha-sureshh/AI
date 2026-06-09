from queue import PriorityQueue

class State:
    def __init__(self, m, c, boat, parent=None):
        self.m, self.c, self.boat, self.parent = m, c, boat, parent

    def is_valid(self):
        rm, rc = 3 - self.m, 3 - self.c
        return (self.m >= 0 and self.c >= 0 and
                (self.m == 0 or self.m >= self.c) and
                (rm == 0 or rm >= rc))

    def is_goal(self):
        return self.m == 0 and self.c == 0

    def __lt__(self, other):
        return False

    def __eq__(self, other):
        return (self.m, self.c, self.boat) == (other.m, other.c, other.boat)

    def __hash__(self):
        return hash((self.m, self.c, self.boat))

    def successors(self):
        s = []
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    nm = self.m - i if self.boat == 'left' else self.m + i
                    nc = self.c - j if self.boat == 'left' else self.c + j
                    nb = 'right' if self.boat == 'left' else 'left'
                    ns = State(nm, nc, nb, self)
                    if ns.is_valid():
                        s.append(ns)
        return s

    def path(self):
        p, cur = [], self
        while cur:
            p.append(cur)
            cur = cur.parent
        return p[::-1]


def best_first_search():
    pq = PriorityQueue()
    start = State(3, 3, 'left')
    pq.put((0, start))
    visited = set()

    while not pq.empty():
        _, state = pq.get()

        if state.is_goal():
            return state.path()

        visited.add(state)

        for nxt in state.successors():
            if nxt not in visited:
                pq.put((len(nxt.path()), nxt))

    return None


def print_solution(sol):
    for i, s in enumerate(sol):
        print("Step", i, ":")
        print("Left side:", s.m, "missionaries and", s.c, "cannibals")
        print("Boat is on the", s.boat, "side.")
        print("Right side:", 3-s.m, "missionaries and", 3-s.c, "cannibals\n")


sol = best_first_search()

if sol:
    print("Solution found:\n")
    print_solution(sol)
else:
    print("No solution found.")
