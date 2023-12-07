from math import prod

games = []

# Each game is broken into a list of dictionaries with the amounts of each cube
with open("chars2.txt", "rt") as file:
    for line in file:
        # Get each draw from the game
        game = line.strip().split(": ")[1].split("; ")
        for i in range(len(game)):
            game[i] = game[i].split(", ")
            draw = game[i]
            
            # Get each cube from the draw
            my_dict = {}
            for cube in draw:
                count, color = cube.split(" ")
                my_dict[color] = int(count)
            game[i] = my_dict
        
        games.append(game)

# Maximum counts for Part 1
max_cube = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

#---------- Part 1 ----------#

solution_p1 = 0
for n, game in enumerate(games, start=1):
    valid = True
    
    for draw in game:
        for color, count in draw.items():
            if count > max_cube[color]:
                # If a color count is greater than its maximum, then the game is invalid
                valid = False
                break
        if not valid: break
    
    if valid:
        solution_p1 += n

print("Part 1:", solution_p1)
