import numpy as np
from numpy import sin, cos, pi, array as arr

DEFAULT_GRID_WIDTH = 10
DEFAULT_GRID_HEIGHT = 10
DEFAULT_DIRECTION_MAP = {
    2:  "N",
    1:  "E",
    -2: "S",
    -1: "W",
}
DEFAULT_MOVEMENT_MAP = {
    "M": 1
}
DEFAULT_ROTATION_MAP = {
    "L": pi/2, 
    "R": -pi/2
}

def execute(
        command: str,
        grid_width: int = DEFAULT_GRID_WIDTH,
        grid_height: int = DEFAULT_GRID_HEIGHT,
        mov_map: dict[str, float] = DEFAULT_MOVEMENT_MAP,
        rot_map: dict[str, float] = DEFAULT_ROTATION_MAP,
        dir_map: dict[float, str] = DEFAULT_DIRECTION_MAP,
    ) -> str:
    """ Simple mars rover solution

    This solution is optimised for fewest lines of code, ty Rowan Lee for the challenge :)
    Obviously there is a lot of wasted compute here, but that was the challenge :)
    This was created using red-green-refactor tdd, look at the commits. 
    This is a 5 line solution, (with some lines spread over multiple lines for readability)

    Args:
        command (str): string of movement/rotation commands
        grid_width (int, optional): grid height
        grid_height (int, optional): grid width
        mov_map (dict[str, float], optional): maps movement commands to a distance to travel in board units
        rot_map (dict[str, float], optional): maps rotation commands to a rotation angle (in radians)
        direction_map (dict[float, str], optional): a float z to a direction, z is derived from rotation vector (x,y) as z = x + 2y

    Returns:
        str: final coordinates and direction as a string in the format "x:y:D",
    """
    loc,rot = arr((0, 0)),arr((0, 1)) # starts at the origin, facing in positive y
    for char in command:
        rot = np.round(arr([[cos(rot_map.get(char,0)),-sin(rot_map.get(char, 0))],[sin(rot_map.get(char, 0)),cos(rot_map.get(char, 0))]])@rot,5)
        loc = np.round(arr(((loc+(mov_map.get(char,0)*rot))[0]%grid_width,(loc+(mov_map.get(char,0)*rot))[1]%grid_height)),5)
    return f"{loc[0]}:{loc[1]}:{dir_map.get(rot[0] + 2 * rot[1], "N")}"
