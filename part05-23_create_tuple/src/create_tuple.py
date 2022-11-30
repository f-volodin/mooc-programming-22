def create_tuple(x: int, y: int, z: int):
    a = min(x,y,z)
    b = max(x,y,z)
    c = x + y + z
    tupl = (a, b, c)
    return tupl