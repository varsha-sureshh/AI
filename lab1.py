def dfs(j1, j2, t, x=0, y=0, vis=None, path=None):
    if vis is None: vis = set()
    if path is None: path = []

    if (x, y) in vis: return False
    vis.add((x, y))

    print("Visiting:", (x, y))

    if x == t or y == t:
        print("\nSolution Found:")
        for a, b in path:
            print(a, b)
        return True

    moves = [
        ("Fill J1", (j1, y)),
        ("Fill J2", (x, j2)),
        ("Empty J1", (0, y)),
        ("Empty J2", (x, 0)),
        ("Pour 1→2", (x - min(x, j2-y), y + min(x, j2-y))),
        ("Pour 2→1", (x + min(y, j1-x), y - min(y, j1-x)))
    ]

    for step, (nx, ny) in moves:
        if dfs(j1, j2, t, nx, ny, vis, path + [(step, (nx, ny))]):
            return True

    return False


j1 = int(input("Enter the capacity of Jug 1: "))
j2 = int(input("Enter the capacity of Jug 2: "))
t = int(input("Enter the target amount: "))

if not dfs(j1, j2, t):
    print("No solution")
