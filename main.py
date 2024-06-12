import heapq

graph = {
    'point1': {'point2': 40, 'point3': 70},
    'point2': {'point1': 40, 'point3': 10},
    'point3': {'point1': 70, 'point2': 10},
}

def dijkstra(graph, start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    shortest_path = {node: [] for node in graph}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path[neighbor] = shortest_path[current_node] + [current_node]
    
    return distances, shortest_path

target = 'point1'
all_distances = {}
all_paths = {}

for start in graph.keys():
    distances, paths = dijkstra(graph, start)
    all_distances[start] = distances[target]
    all_paths[start] = paths[target] + [target]

for start in all_distances:
    print(f"Kürzeste Distanz von {start} nach point1: {all_distances[start]} km")
    print(f"Pfad: {' -> '.join(all_paths[start])}")
    print()
