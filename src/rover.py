compass_directions = ["N", "E", "S", "W"]

def execute(
        command: str,
        grid_width: int = 10,
        grid_height: int = 10,
    ) -> str:
    '''simple mars rover solution'''
    x = 0
    y = 0 
    direction = 0
    for char in list(command):
        if char == "M":
            if direction % 2 == 0:
                y = (y + (1 - (direction % len(compass_directions)))) % grid_height
            else:
                x = (x + (2 - (direction % len(compass_directions)))) % grid_width          
        elif char == "L":
            direction = (direction - 1) % len(compass_directions)
        elif char == "R": 
            direction = (direction + 1) % len(compass_directions)

    return f"{x}:{y}:{compass_directions[direction]}"
