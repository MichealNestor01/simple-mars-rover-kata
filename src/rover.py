compass_directions = ["N", "E", "S", "W"]

def execute(command: str) -> str:
    x = 0
    y = 0 
    direction = 0
    for char in list(command):
        if char == "M":
            x += 1
        elif char == "L":
            direction = (direction - 1) % len(compass_directions)
            
    return f"0:{x}:{compass_directions[direction]}"
