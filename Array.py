from Value import Value


class Array:
    def __init__(self, values):
        if not all(isinstance(v, Value) for v in values):
            raise TypeError("Input a list of Value instances!")
        self.values = values

    def __repr__(self):
        return f"Array vales: {self.values}"

    def __add__(self, other):
        return Array(self.values + other.values)

    def __mul__(self, other):
        return Array(self.values * other.values)
