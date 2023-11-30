class Value:
    def __init__(self, data: float, _children=(), _op="", label=""):
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.label = label

    def __repr__(self) -> str:
        return f"Value data: {self.data}"

    def __str__(self) -> str:
        return f"Value data: {self.data}"

    def __add__(self, other):
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        return Value(self.data * other.data, (self, other), "*")

    def __neg__(self):  # -self
        return self * -1

    def __radd__(self, other) -> float:  # other + self
        return self + other

    def __sub__(self, other):  # self - other
        return self + (-other)

    def __rsub__(self, other) -> float:  # other - self
        return other + (-self)

    def __rmul__(self, other) -> float:  # other * self
        return self * other

    def __truediv__(self, other) -> float:  # self / other
        return self * other ** -1

    def __rtruediv__(self, other) -> float:  # other / self
        return other * self ** -1

    @property
    def prev(self):
        return self._prev

    @property
    def op(self):
        return self._op


v1 = Value(3, label="v1")
v2 = Value(4, label="v2")
v3 = v1 + v2
print(v3.prev)
print(v3.op)
