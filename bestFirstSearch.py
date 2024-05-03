def bestFirstSearch(graph, start, end) : 
    cities = [] # Cities that are visited
    current_node = start
    path = [start] # final path --> solution
    cost = 0 # total cost
    while current_node is not end :
        cities.append(current_node) # add current node to cities
        neighbors = graph[current_node] # sub-dictionary of neighbors
        
        # Find neighbor with minimal cost
        min_cost = float("inf")
        next_node = None # empty, nothing, no solution
        for neighbor, dist in neighbors.items() :
            if neighbor not in cities and dist < min_cost :
                min_cost = dist
                next_node = neighbor
        
        # Update path and return final result 
        if next_node is None :
            return None, float('inf') # No path found
        cost += min_cost
        path.append(next_node)
        current_node = next_node
    return path, cost, cities
