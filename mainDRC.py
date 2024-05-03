from astar import astar
from bestFirstSearch import bestFirstSearch
from greedyBestFirstSearch import greedyBestFirstSearch

graph = {
    "Kisangani": {
        "Goma": 87
    },
    "Goma": {
        "Bukavu": 92,
        "Kisangani": 87,
    },
    "Bukavu": {
        "Goma": 92,
        "Likasi": 142,
    },
    "Likasi": {
        "Bukavu": 142,
        "Lubumbashi": 98,
        "Kolwezi": 85,
    },
    "Lubumbashi": {
        "Likasi": 98,
        "Kasumbalesa": 86,
    },
    "Kasumbalesa": {
        "Lubumbashi": 86
    },
    "Kolwezi": {
        "Likasi": 85,
        "Mbuji-Mayi": 211,
        "Kamina": 101,
        "Kundelungu": 90,
    },
    "Kundelungu": {
        "Kolwezi": 90
    },
    "Mbuji-Mayi": {
        "Kolwezi": 211,
        "Kananga": 99,
    },
    "Kamina": {
        "Kolwezi": 101,
        "Mwene-Ditu": 138,
        "Tshikapa": 97,
    },
    "Kananga": {
        "Mbuji-Mayi": 99,
        "Tshikapa": 80,
        "Kinshasa": 140,
        "Mbandaka": 151,
    },
    "Tshikapa": {
        "Kananga": 80,
        "Kamina": 97,
        "Mwene-Ditu": 146,
    },
    "Mwene-Ditu": {
        "Tshikapa": 146,
        "Kamina": 138,
        "Idiofa": 120,
    },
    "Mbandaka": {
        "Kananga": 151,
        "Bandundu": 71, 
    },
    "Bandundu": {
        "Mbandaka": 71,
        "Kinshasa": 75,
    },
    "Kinshasa": {
        "Bandundu": 75,
        "Kananga": 140,
        "Matadi": 118,
    },
    "Matadi": {
        "Kinshasa": 118,
        "Boma": 111,
    },
    "Boma": {
        "Matadi": 111,
        "Kikwit":70,
    },
    "Kikwit": {
        "Boma": 70,
        "Idiofa": 75,
    },
    "Idiofa": {
        "Kikwit": 75,
        "Mwene-Ditu": 120,
    
    }
}

start = 'Kananga'
end = 'Mwene-Ditu'

results = [bestFirstSearch(graph, start, end)]

for result in results:
    if result[0]:
        print("Path from ", start, " to ", end, ": ")
        for i in result[0]:
            print("- ", i)

        print("Total cost: ", result[1])
    else:
        print("No path found from ", start, " to ", end)
    
    print("/n /n")   


