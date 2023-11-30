from Value import Value
import math


class Vector:
    def __init__(self, *values: Value) -> None:

        if not all(isinstance(v, Value) for v in values):
            raise TypeError("Input a list of Value instances!")
        self.values = values

    def __repr__(self) -> str:
        return f"Vector: {' '.join(map(str, self.values))}"

    def __str__(self) -> str:
        return f"Vector: {' '.join(map(str, self.values))}"

    def __add__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("The length of the vectors must be the same.")
        return Vector(*[x + y for x, y in zip(self.values, other.values)])

    def __sub__(self, other):
        if len(self.values) != len(other.values):
            raise ValueError("The length of the vectors must be the same.")
        return Vector(*[x - y for x, y in zip(self.values, other.values)])

    def dot(self, other) -> float:
        if len(self.values) != len(other.values):
            raise ValueError("The length of the vectors must be the same.")
        return sum(*[x * y for x, y in zip(self.values, other.values)])

    def magnitude(self):
        return math.sqrt(sum(x * x for x in self.values))
