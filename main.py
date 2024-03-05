class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y


class Figure2D:
    def __init__(self, points: list[Point]):
        self._points = points
        self._sides = []

        for i in range(len(points)):
            p_a = points[i-1]
            p_b = points[i]
            self._sides.append((abs(p_a.x - p_b.x)**2 + abs(p_a.y - p_b.y)**2)**0.5)

    @property
    def sides(self) -> list[float]:
        return self._sides

    @property
    def points(self) -> list[Point]:
        return self._points

    def area(self) -> float:
        raise RuntimeError()

    def is_intersect(self, figure) -> bool:
        p_a: list[Point] = self.points
        p_b: list[Point] = figure.points
        for i in range(len(p_a)):
            for j in range(len(p_b)):
                p11 = p_a[i-1]
                p12 = p_a[i]
                p21 = p_b[j-1]
                p22 = p_b[j]
                m1 = (p12.y - p11.y) / (p12.x - p11.x)
                m2 = (p22.y - p21.y) / (p22.x - p21.x)
                c1 = p11.y - m1 * p11.x
                c2 = p21.y - m2 * p21.x

                if m1 == m2 and c1 != c2:
                    return True
                else:
                    return False

    def compare(self, figure) -> int:
        a1 = self.area()
        a2 = figure.area()
        if a1 > a2:
            return 1
        elif a1 == a2:
            return 0
        else:
            return -1


class Pentagon(Figure2D):
    def __init__(self, points: list[Point]):
        super().__init__(points)
        if len(points) != 5:
            raise RuntimeError()

    def area(self) -> float:
        return super().sides[0]**2 / 4 * (25 + 10 * 5**0.5)**0.5


class Triangle(Figure2D):
    def __init__(self, points: list[Point]):
        super().__init__(points)
        if len(points) != 3:
            raise RuntimeError()

    def area(self) -> float:
        sides = super().sides
        p = sum(sides) / 2
        area = 1
        for v in map(lambda side: p - side, sides):
            area *= v
        return (p * area)**0.5
