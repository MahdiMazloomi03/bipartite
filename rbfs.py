# -*- coding: utf-8 -*-
"""RBFS.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WrqnZDl_IRDwd2z__uBQ_vLSygZgypUB
"""

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu vilcea': 80},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Rimnicu vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Craiova': {'Drobeta': 120, 'Rimnicu vilcea': 146, 'Pitesti': 138},
    'Bucharest': {'Pitesti': 101, 'Fagaras': 211, 'Giurgiu': 90, 'Urziceni': 85},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Neamt': {'Iasi': 87},
    'Pitesti': {'Bucharest': 101, 'Rimnicu vilcea': 97, 'Craiova': 138},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Eforie': {'Hirsova': 86},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Fagaras': {'Sibiu': 99}  # Add missing node
}

heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Sibiu': 253,
    'Timisoara': 329,
    'Oradea': 380,
    'Fagaras': 176,
    'Rimnicu vilcea': 193,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234,
}

def ida_star(graph, heuristic, start, goal):
    def search(node, g, threshold, path):
        f = g + heuristic[node]
        if f > threshold:
            return f
        if node == goal:
            return "Goal"
        min_val = float('inf')
        for neighbor, cost in graph[node].items():
            if neighbor not in path:
                path.append(neighbor)
                result = search(neighbor, g + cost, threshold, path)
                if result == "Goal":
                    return "Goal"
                if result < min_val:
                    min_val = result
                path.pop()
        return min_val

    path = [start]
    threshold = heuristic[start]
    while True:
        result = search(start, 0, threshold, path)
        if result == "Goal":
            return path
        if result == float('inf'):
            return "No path found"
        threshold = result


start_city = 'Neamt'
goal_city = 'Bucharest'
shortest_path = ida_star(graph, heuristic, start_city, goal_city)
print(f"Shortest path from {start_city} to {goal_city}: {shortest_path}")

