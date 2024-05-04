from astar import astar
from bestFirstSearch import bestFirstSearch
from greedyBestFirstSearch import greedyBestFirstSearch


graph = {
    "New York City" : {
        "Chicago" : 1146,
        "Houston" : 2547
    },
    "Los Angeles": {
        "Chicago" : 2786,
        "Houston" : 2249,
        "Phoenix" : 373
    },
    "Chicago": {
        "New York City" : 1146,
        "Houston" : 1483,
        "Phoenix" : 2835,
        "Los Angeles" : 2786
    },
    "Phoenix" : {
        "Los Angeles" : 373,
        "Chicago" : 2835,
        "Houston" : 1804
    },
    "Houston" : {
        "New York City" : 2547,
        "Chicago" : 1483,
        "Los Angeles" : 2249,
        "Phoenix" : 1804
    }
}

coordinates = {
    "New York City" : (40.7128, -74.0060),
    "Houston" : (29.7604, -95.3698),
    "Phoenix" : (33.4484, -112.0740),
    "Los Angeles" : (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298)
}

# """
start = 'Phoenix'
end = 'Los Angeles'

results = [bestFirstSearch(graph, start, end), greedyBestFirstSearch(graph, start, end, coordinates), astar(graph, start, end, coordinates)]

for result in results:
    if result[0]:
        print("Path from ", start, " to ", end, ": ")
        for i in result[0]:
            print("- ", i)

        print("Total cost: ", result[1])
    else:
        print("No path found from ", start, " to ", end)
     
    print("\n -------------------------------------------------- \n")

"""

open = True

while open:
    print("--------------------------------------------------------------------------------")
    print("| ---------- TROUVER LE CHEMIN LE MOINS COUTEUX GRACE A CE LOGICIEL ---------- |")
    print("--------------------------------------------------------------------------------")
    start = input("1. Entres ta ville de départ: ")
    end = input("2. Entres ta ville de destination: ")
    print("--------------------------------------------------------------------------------")
    if start in graph and end in graph:
        message = f"Pour sortir de {start} vers {end}"
        print(message)
        results = [bestFirstSearch(graph, start, end), greedyBestFirstSearch(graph, start, end, coordinates), astar(graph, start, end, coordinates)]

        for result in results:
            print(result)

            print("--------------------------------------------------------------------------------")
        print("Voilà nos suggestions en matière d'itineraire. ")
        open=False

        
    else: 
        message = "Entrer des villes existantes dans notre graph"
        print(message)
        open = False
    
print("--------------------------------------------------------------------------------")
"""