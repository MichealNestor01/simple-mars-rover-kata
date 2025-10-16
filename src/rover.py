compass_directions = ["N", "E", "S", "W"]

def execute(command: str) -> str:
    x = 0
    y = 0 
    direction = 0
    for char in list(command):
        if char == "M":
            if direction % 2 == 0:
                y += 1 - (direction % len(compass_directions))
            else:
                x += 2 - (direction % len(compass_directions))
        elif char == "L":
            direction = (direction - 1) % len(compass_directions)
        elif char == "R": 
            direction = (direction + 1) % len(compass_directions)

    return f"{x}:{y}:{compass_directions[direction]}"
