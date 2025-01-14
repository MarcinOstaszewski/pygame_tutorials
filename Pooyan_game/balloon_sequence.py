import random

positions = [200, 400, 600, 800]

balloon_sequence = [
    {'color': 'blue', 'position_x': random.choice(positions), 'time': 3},
    {'color': 'red', 'position_x': random.choice(positions), 'time': 5},
    {'color': 'orange', 'position_x': random.choice(positions), 'time': 7},
    {'color': 'blue', 'position_x': random.choice(positions), 'time': 9},
    {'color': 'red', 'position_x': random.choice(positions), 'time': 11},
    {'color': 'orange', 'position_x': random.choice(positions), 'time': 13},
    {'color': 'blue', 'position_x': random.choice(positions), 'time': 15},
    {'color': 'red', 'position_x': random.choice(positions), 'time': 17},
    {'color': 'orange', 'position_x': random.choice(positions), 'time': 19},
    {'color': 'blue', 'position_x': random.choice(positions), 'time': 21},
]
