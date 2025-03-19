class Circle:
    def __init__(self, radius: float):
        self.type = 'circle'
        self.radius = radius

class Square:
    def __init__(self, side: float):
        self.type = 'square'
        self.side = side

def get_area(s: Square|Circle) -> float:
    if s.type == 'circle':
        assert isinstance(s, Circle)
        return s.radius ** 2 * 3.14
    else:
        assert isinstance(s, Square)
        return s.side ** 2

print(get_area(Circle(1.2)))

def get_area2(s: Square|Circle) -> float:
    if isinstance(s, Circle):
        return s.radius ** 2 * 3.14
    elif isinstance(s, Square):
        return s.side ** 2
    else:
        raise TypeError(f"Received object {s} of unknown type {type(s)}")
