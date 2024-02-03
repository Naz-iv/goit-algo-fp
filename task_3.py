import heapq


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex, weight):
        if weight is None:
            weight = 0
        self.vertices[from_vertex].append((to_vertex, weight))
        self.vertices[to_vertex].append((from_vertex, weight))


def dijkstra(graph: Graph, start):
    distances = {vertex: float("infinity") for vertex in graph.vertices}
    distances[start] = 0
    unvisited = [(0, start)]

    while unvisited:
        current_distance, current_vertex = heapq.heappop(unvisited)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.vertices[current_vertex]:
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(unvisited, (distance, neighbor))

    return distances


def execute():
    cities = {
        "Київ": {"Чернігів": 145, "Житомир": 132, "Черкаси": 198, "Полтава": 345},
        "Чернігів": {"Київ": 145, "Суми": 230, "Черкаси": 180},
        "Житомир": {"Київ": 132, "Рівне": 245, "Вінниця": 310},
        "Черкаси": {"Київ": 198, "Кропивницький": 250, "Чернігів": 180},
        "Полтава": {"Київ": 345, "Харків": 290, "Суми": 220},
        "Суми": {"Чернігів": 230, "Харків": 150, "Полтава": 220},
        "Рівне": {"Луцьк": 270, "Житомир": 245, "Тернопіль": 315},
        "Вінниця": {"Житомир": 310, "Хмельницький": 180, "Чернівці": 420},
        "Кропивницький": {"Черкаси": 250, "Миколаїв": 160, "Дніпро": 310},
        "Харків": {"Суми": 150, "Полтава": 290, "Дніпро": 345},
        "Луцьк": {"Рівне": 270, "Житомир": 390, "Тернопіль": 340},
        "Хмельницький": {"Вінниця": 180, "Тернопіль": 120, "Чернівці": 220},
        "Чернівці": {"Львів": 385, "Івано-Франківськ": 250, "Хмельницький": 220},
        "Тернопіль": {"Луцьк": 340, "Рівне": 315, "Хмельницький": 120},
    }

    districts_map = Graph()

    for city in cities:
        districts_map.add_vertex(city)

    for city, connections in cities.items():
        for connected_city, distance in connections.items():
            if connected_city not in cities:
                districts_map.add_vertex(connected_city)
            districts_map.add_edge(city, connected_city, weight=distance)

    return districts_map


if __name__ == "__main__":
    country_graph = execute()

    for start_city in country_graph.vertices:
        shortest_paths = dijkstra(country_graph, start_city)
        print(f"Найкоротші шляхи від `{start_city}`: {shortest_paths}")
