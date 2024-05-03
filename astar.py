import math



def haversine(lat1, lon1, lat2, lon2):
    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    R = 6371 # earth radius in kilometers
    distance = 2*R*math.asin(math.sqrt(a))
    return distance

def heuristic(A,B):
    lat1, lon1 = coordinates[A]
    lat2, lon2 = coordinates[B]
    
    return haversine(lat1, lon1, lat2, lon2)


def astar(graph, start, end) : 
    cities = [] # Cities that are visited
    current_node = start
    path = [start] # final path --> solution
    cost = 0 # total cost
    while current_node is not end :
        cities.append(current_node) # add current node to cities
        neighbors = graph[current_node] # sub-dictionary of neighbors
        
        # Find neighbor with minimal cost
        min_cost = float("inf")
        min_heuristic = float('inf')
        next_node = None # empty, nothing, no solution
        for neighbor, dist in neighbors.items() :
            dist_heuristic = heuristic(neighbor, end) + dist
            if neighbor not in cities and dist_heuristic < min_heuristic :
                min_cost = dist
                min_heuristic = dist_heuristic
                next_node = neighbor
        
        # Update path and return final result 
        if next_node is None :
            return None, float('inf') # No path found
        cost += min_cost
        path.append(next_node)
        current_node = next_node
    return path, cost, cities

start = 'Los Angeles'
end = 'New York City'

result = astar(graph, start, end)

if result[0]:
    print("Path from ", start, " to ", end, ": ")
    for i in result[0]:
        print("- ", i)
    
    print("Total cost: ", result[1])
else:
    print("No path found from ", start, " to ", end)
    
