compass_directions = ["N", "E", "S", "W"]

def execute(
        command: str,
        grid_width: int = 10,
        grid_height: int = 10,
    ) -> str:
    '''simple mars rover solution'''
    _direction_map = {"L": -1, "R": 1}
    _compass_directions = ["N", "E", "S", "W"]
    x = 0
    y = 0 
    direction = 0
    for char in list(command):
        if char == "M":
            if direction % 2 == 0:
                y = (y + (1 - (direction % len(_compass_directions)))) % grid_height
            else:
                x = (x + (2 - (direction % len(_compass_directions)))) % grid_width  
        direction = (direction + _direction_map.get(char, 0)) % len(_compass_directions)


    return f"{x}:{y}:{_compass_directions[direction]}"
