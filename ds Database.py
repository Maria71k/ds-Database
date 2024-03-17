class Bird:
    def __init__(self, species, color):
        self.species = species
        self.color = color

# Database of birds
birds = [
    Bird("sparrow", "brown"),
    Bird("parrot", "green"),
    Bird("owl", "gray"),
]

# Print information about each bird
for bird in birds:
    print(f"Species: {bird.species}, Color: {bird.color}")
