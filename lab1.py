def pour_water_dfs(j1, j2, target, x=0, y=0, visited=None, path=None):
    if visited is None:
        visited = set()

    if path is None:
        path = []

    if (x, y) in visited:
        return False

    visited.add((x, y))

    print("Visiting:", (x, y))  # DEBUG

    if x == target or y == target:
        print("\nSolution Found:")
        for step, state in path:
            print(step, state)
        return True

    # Fill Jug 1
    if pour_water_dfs(
        j1, j2, target, j1, y,
        visited,
        path + [("Fill J1", (j1, y))]
    ):
        return True

    # Fill Jug 2
    if pour_water_dfs(
        j1, j2, target, x, j2,
        visited,
        path + [("Fill J2", (x, j2))]
    ):
        return True

    # Empty Jug 1
    if pour_water_dfs(
        j1, j2, target, 0, y,
        visited,
        path + [("Empty J1", (0, y))]
    ):
        return True

    # Empty Jug 2
    if pour_water_dfs(
        j1, j2, target, x, 0,
        visited,
        path + [("Empty J2", (x, 0))]
    ):
        return True

    # Pour Jug 1 → Jug 2
    pour = min(x, j2 - y)
    if pour_water_dfs(
        j1, j2, target,
        x - pour, y + pour,
        visited,
        path + [("Pour 1→2", (x - pour, y + pour))]
    ):
        return True

    # Pour Jug 2 → Jug 1
    pour = min(y, j1 - x)
    if pour_water_dfs(
        j1, j2, target,
        x + pour, y - pour,
        visited,
        path + [("Pour 2→1", (x + pour, y - pour))]
    ):
        return True

    return False


# MAIN PROGRAM
j1 = int(input("Enter the capacity of Jug 1: "))
j2 = int(input("Enter the capacity of Jug 2: "))
target = int(input("Enter the target amount: "))

if not pour_water_dfs(j1, j2, target):
    print("No solution")
