n = int(input("Enter number of movies: "))

movies = {}

# Input movie details
for i in range(n):
    name = input("\nEnter movie name: ")
    year = int(input("Enter release year: "))
    director = input("Enter director name: ")
    cost = float(input("Enter production cost: "))
    collection = float(input("Enter collection made: "))

    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

# 1) Print all movie details
print("\nAll Movie Details:")
for name, details in movies.items():
    print(name, "->", details)

# 2) Movies released before 2015
print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

# 3) Movies that made profit
print("\nMovies that made profit:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

# 4) Movies by a particular director
d = input("\nEnter director name to search: ")

print("Movies directed by", d, ":")
for name, details in movies.items():
    if details["director"].lower() == d.lower():
        print(name)