class Value:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"Value data: {self.data}"

    def __add__(self, other):
        return Value(self.data + other.data)

    def __mul__(self, other):
        return Value(self.data * other.data)


v1 = Value(3)
v2 = Value(4)
print(v1+v2)