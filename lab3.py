import heapq

# --- Graph: Romania Map ---
romania_map = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99),
              ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101)]
}

# --- Heuristic: Straight-line distance to Bucharest ---
h_sld = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Fagaras': 176,
    'Lugoj': 244,
    'Mehadia': 241,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Zerind': 374
}

# --- A* Algorithm ---
def astar(start, goal):
    frontier = [(h_sld[start], start, [start], 0)]  # (f, node, path, g)
    explored = set()

    while frontier:
        f, current, path, g = heapq.heappop(frontier)

        if current == goal:
            return path, g

        if current not in explored:
            explored.add(current)

            for neighbor, dist in romania_map.get(current, []):
                new_g = g + dist
                new_f = new_g + h_sld[neighbor]

                heapq.heappush(
                    frontier,
                    (new_f, neighbor, path + [neighbor], new_g)
                )

    return None, float('inf')


# --- Run A* ---
path, cost = astar('Arad', 'Bucharest')

print("Optimal Path:" , "->".join(path))
print("Total Cose:", cost, "km"
