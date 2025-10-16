def execute(command: str) -> str:
    x = 0
    y = 0 
    direction = ""
    for char in list(command):
        if char == "M":
            x += 1
    return f"0:{x}:N"
