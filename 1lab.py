class Route:
    def __init__(self, start, finish, *distances):
        self.start = start
        self.finish = finish
        self.distances = list(distances)

    def __str__(self):
        total_length = sum(self.distances)
        num_stops = len(self.distances) + 1  
        return f"Маршрут: {self.start} -> {self.finish}, довжина: {total_length} км, кількість привалів: {num_stops}"

    def total_length(self):
        return sum(self.distances)

    def num_stops(self):
        return len(self.distances) + 1

    def longest_segment(self):
        longest = self.distances[0]
        for distance in self.distances:
            if distance > longest:
                longest = distance
        return longest

    def __lt__(self, other):
        return self.total_length() < other.total_length()

    def __eq__(self, other):
        return self.total_length() == other.total_length()

    def __gt__(self, other):
        return self.total_length() > other.total_length()

def routes_with_max_stops(routes):
    max_stops = routes[0].num_stops()
    for route in routes:
        if route.num_stops() > max_stops:
            max_stops = route.num_stops()
    max_routes = []
    for route in routes:
        if route.num_stops() == max_stops:
            max_routes.append(route)
    return max_routes

def route_with_longest_segment(routes):
    longest_route = routes[0]
    for route in routes:
        if route.longest_segment() > longest_route.longest_segment():
            longest_route = route
    return longest_route

def routes_start_or_end(routes, point):
    result_routes = []
    for route in routes:
        if route.start == point or route.finish == point:
            result_routes.append(route)
    return result_routes

routes = [
    Route("Кваси", "Дземброня", 8, 8, 12, 18, 12),
    Route("Івано-Франківськ", "Яремче", 15, 10, 7),
    Route("Сколе", "Львів", 30, 40),
    Route("Чернівці", "Молдава", 50, 60, 70),
    Route("Рахів", "Богдан", 10, 20, 15),
    Route("Чернівці", "Івано-Франківськ", 25, 30, 20),
    Route("Дземброня", "Говерла", 12, 18, 20),
    Route("Старий Люблін", "Тернопіль", 15, 20, 12, 8),
    Route("Хуст", "Синевир", 8, 13, 7),
    Route("Славське", "Тисовиця", 5, 10, 5),
]

routes.sort()

for route in routes:
    print(route)

print("\nМаршрути з максимальною кількістю привалів:")
for route in routes_with_max_stops(routes):
    print(route)

print("\nМаршрут з найдовшим переходом:")
print(route_with_longest_segment(routes))

print("\nМаршрути, що починаються або закінчуються в точці 'Чернівці':")
for route in routes_start_or_end(routes, "Чернівці"):
    print(route)
